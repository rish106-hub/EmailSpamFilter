# Email Spam Filter

**Email Spam Filter** is a Flask-based web application made using GenAI that uses machine learning to classify messages as **Spam** or **Not Spam**. The project features a modern, responsive UI with animations and demonstrates the integration of Flask and machine learning.

---

## Features

- **Real-time Spam Detection**: Classifies user-inputted messages as **Spam** or **Not Spam**.
- **Modern UI**: Responsive and visually appealing design with smooth animations.
- **Machine Learning**: Trained using Logistic Regression with SMOTE for class balancing.
- **Text Preprocessing**: Incorporates cleaning, tokenization, and TF-IDF vectorization.

---

## Technologies Used

- **Backend**: Flask, Python
- **Frontend**: HTML5, CSS3
- **Machine Learning**: Scikit-learn, Imbalanced-learn (SMOTE)
- **Tools**: pandas, NLTK, TfidfVectorizer

---

## How to Run Locally

Follow these steps to set up and run the project on your local machine:

### 1. Clone the Repository
```bash
git clone https://github.com/rish106-hub/EmailSpamFilter.git
cd EmailSpamFilter
python3 -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate     # For Windows
pip install -r requirements.txt
cd app
python3 app.py
