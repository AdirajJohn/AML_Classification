from flask import Flask, request, render_template, jsonify
from flask_cors import CORS, cross_origin
import os
from AML_Classifier.pipeline.prediction import PredictionPipeline
import pickle

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)

# Landing page
@app.route("/")
@cross_origin()
def home():
    return render_template('index.html')

# Prediction endpoint
@app.route('/predict', methods=['POST'])
@cross_origin()
def predict():
    try:
        # Get form data
        form_data = request.form.to_dict()
        
        # Convert numeric values to the appropriate type
        for key in ['from_bank', 'to_bank', 'amount_received', 'amount_paid']:
            form_data[key] = float(form_data[key])

        #Initialize the ClientApp
        pred = PredictionPipeline(form_data)

        # Prediction using the classifier instance in ClientApp
        prediction = pred.predict()

        return jsonify({'prediction': prediction})
    
    except Exception as e:
        return str(e), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)


