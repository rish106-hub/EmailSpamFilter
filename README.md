Email Spam Filter

A Flask-based web application that detects whether a message is Spam or Not Spam using a trained machine learning model. This project demonstrates the integration of natural language processing (NLP) techniques with Flask to build an interactive web app.

Features

Real-time Spam Detection: Enter a message and get instant classification as Spam or Not Spam.
Modern UI: A clean, responsive interface with smooth animations.
Machine Learning: Uses Logistic Regression with SMOTE to handle class imbalance.
Text Preprocessing: Incorporates text cleaning, tokenization, and TF-IDF vectorization.
Tech Stack

Backend: Flask, Python
Frontend: HTML5, CSS3
Machine Learning: Scikit-learn, Imbalanced-learn (SMOTE)
Deployment Ready: Compatible with platforms like Heroku, Render, and AWS.
How to Run Locally

Follow these steps to set up and run the project locally:

1. Clone the Repository
git clone https://github.com/rish106-hub/EmailSpamFilter.git
cd EmailSpamFilter
2. Set Up a Virtual Environment
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
3. Install Dependencies
pip install -r requirements.txt
4. Run the Flask Application
cd app
python3 app.py
5. Access the Application
Open your browser and go to:

http://127.0.0.1:5000/
Project Structure

EmailSpamFilter/
├── app/
│   ├── templates/       # HTML templates
│   ├── static/          # CSS and other static assets
│   └── app.py           # Flask application
├── data/
│   ├── spam.csv         # Dataset
│   └── preprocessed/    # Preprocessed files
├── models/
│   └── improved_spam_classifier.pkl  # Trained model
├── src/
│   ├── data_loading.py  # Script to load data
│   ├── preprocessing.py # Script for data preprocessing
│   └── improve_model.py # Script to train and improve the model
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
Screenshots

Home Page
Prediction Result
Future Enhancements

Deploy to Cloud: Host the application on platforms like Heroku or AWS.
Add Support for Multiple Languages: Extend spam detection to messages in other languages.
Advanced Models: Experiment with transformer-based models like BERT for improved accuracy.
License

This project is open-source and available under the MIT License. Feel free to fork, modify, and use it as per your requirements.
