from flask import Flask, render_template, request
from src.predict import predict_email

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        email = request.form.get('email')
        if email:
            prediction = predict_email('models/phishing_detector.pkl', 'data/preprocessed_data.pkl', email)
    return render_template('index.html', prediction=prediction)

@app.route('/slides')
def slides():
    return render_template('slides.html')

if __name__ == '__main__':
    app.run(debug=True)
