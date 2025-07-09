from flask import Flask, render_template, request
from src.predict import predict_email

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    email_text = request.form.get('email')
    if not email_text:
        return render_template('index.html', error="Email text is required.")
    result = predict_email("models/phishing_detector.pkl", "data/preprocessed_data.pkl", email_text)
    return render_template('index.html', result=result, email=email_text)

@app.route('/awareness')
def awareness():
    return render_template('awareness.html')

if __name__ == '__main__':
    app.run(debug=True)
