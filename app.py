from flask import Flask, request, render_template
import os
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Load the trained model and vectorizer
project_dir = os.path.expanduser("~/Developer/EmailSpamFilter")
model_path = os.path.join(project_dir, "models", "improved_spam_classifier.pkl")
vectorizer_path = os.path.join(project_dir, "data", "preprocessed", "vectorizer.pkl")

model = pd.read_pickle(model_path)
vectorizer = pd.read_pickle(vectorizer_path)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
@app.route('/predict', methods=['POST'])
def predict():
    # Get the message from the form
    message = request.form['message']
    # Transform the message using the vectorizer
    message_tfidf = vectorizer.transform([message])
    # Predict using the trained model
    prediction = model.predict(message_tfidf)[0]
    # Map prediction to label
    result = "Spam" if prediction == 1 else "Not Spam"  # Updated label
    return render_template('index.html', prediction=result, message=message)

if __name__ == '__main__':
    app.run(debug=True)
