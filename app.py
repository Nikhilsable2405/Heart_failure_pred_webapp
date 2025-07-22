from flask import Flask, render_template, request
import pickle
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
model = pickle.load(open('heart_model.pkl', 'rb'))

# Load the scaler
scaler = pickle.load(open('scaler.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Retrieve form inputs and convert to float
        features = [float(request.form.get(i)) for i in [
            'age', 'anaemia', 'creatinine_phosphokinase', 'diabetes',
            'ejection_fraction', 'high_blood_pressure', 'platelets',
            'serum_creatinine', 'serum_sodium', 'sex', 'smoking', 'time'
        ]]

        # Convert to numpy array and reshape
        input_data = np.array(features).reshape(1, -1)

        # Scale the input data using the saved scaler
        scaled_input = scaler.transform(input_data)

        # Predict using the model
        prediction = model.predict(scaled_input)[0]

        # Output message
        result = "✅ Patient is likely to survive." if prediction == 0 else "⚠️ High risk of heart failure."
        return render_template('index.html', prediction_text=result)

    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)
