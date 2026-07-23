# 🛍️ Product Review Analysis & Smart Recommendation System

## 📌 Project Overview

The **Product Review Analysis & Smart Recommendation System** is an AI-powered web application that analyzes customer reviews, predicts their sentiment, and recommends relevant products based on review similarity.

This project combines **Machine Learning**, **Natural Language Processing (NLP)**, and **Flask** to help users make informed purchasing decisions. Customer reviews are classified into **Positive**, **Neutral**, or **Negative** sentiments using a Support Vector Machine (SVM) model, while a recommendation engine suggests similar products using TF-IDF vectorization and Cosine Similarity.

---

## ✨ Features

- 🔍 Analyze customer product reviews
- 😊 Predict sentiment (Positive, Neutral, Negative)
- 🤖 Smart product recommendation system
- 📊 Machine Learning-based sentiment analysis
- ⚡ Fast and accurate predictions
- 🌐 User-friendly Flask web interface
- 📱 Responsive and modern UI
- 💬 Real-time review analysis

---

## 🛠️ Tech Stack

### Programming Language
- Python

### Machine Learning & NLP
- Scikit-learn
- Support Vector Machine (SVM)
- TF-IDF Vectorization
- Cosine Similarity
- Pandas
- NumPy

### Web Development
- Flask
- HTML5
- CSS3
- JavaScript

### Tools
- Git
- GitHub
- VS Code
- Google Colab
- Jupyter Notebook

---

## 📂 Project Structure

```
Product-Review-Analysis-System/
│
├── flask_app.py
├── requirements.txt
├── productttt.csv
├── svm_sentiment_modellll.pkl
├── tfidf_vectorizerrrr.pkl
├── recommendtf.pkl
│
├── templates/
│   └── pred.html
│
├── static/
│   ├── css/
│   ├── images/
│   └── js/
│
├── screenshots/
│   ├── home.png
│   ├── input.png
│   ├── prediction.png
│   └── recommendation.png
│
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/Product-Review-Analysis-System.git
```

### 2️⃣ Navigate to the Project Folder

```bash
cd Product-Review-Analysis-System
```

### 3️⃣ Create a Virtual Environment (Optional)

```bash
python -m venv venv
```

### 4️⃣ Activate the Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 5️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 6️⃣ Run the Application

```bash
python flask_app.py
```

### 7️⃣ Open in Browser

```
http://127.0.0.1:5000
```

---

## 🚀 How It Works

1. User enters a product review.
2. The review is cleaned and preprocessed.
3. TF-IDF converts the review into numerical features.
4. The trained SVM model predicts the sentiment.
5. Cosine Similarity identifies similar products.
6. The application displays personalized product recommendations.

---

## 📊 Machine Learning Workflow

```
User Review
      │
      ▼
Text Preprocessing
      │
      ▼
TF-IDF Vectorization
      │
      ▼
SVM Sentiment Prediction
      │
      ▼
Cosine Similarity
      │
      ▼
Recommended Products
```

---
## 📈 Model Details

| Model | Purpose |
|--------|---------|
| Support Vector Machine (SVM) | Sentiment Classification |
| TF-IDF Vectorizer | Text Feature Extraction |
| Cosine Similarity | Product Recommendation |

---

## 🎯 Skills Demonstrated

- Python Programming
- Machine Learning
- Natural Language Processing (NLP)
- Flask Web Development
- HTML & CSS
- Data Preprocessing
- Feature Engineering
- REST API Development
- Git & GitHub
- Debugging & Testing
- Software Development
- Problem Solving

---

## 🚀 Future Improvements

- User Authentication
- Database Integration (MySQL)
- Advanced Recommendation Algorithms
- BERT-based Sentiment Analysis
- Real-time Product Reviews
- Cloud Deployment (Render/AWS)
- Admin Dashboard
- Multilingual Review Support

---

## 📚 Dataset

The project uses the **Women's E-Commerce Clothing Reviews** dataset from Kaggle for training and evaluation.

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Push to your branch.
5. Open a Pull Request.

---

## 👩‍💻 Author

**Eedupuganti Divya Sai Sandhya**

📧 Email: your-email@example.com

💼 LinkedIn: https://linkedin.com/in/your-linkedin-profile

💻 GitHub: https://github.com/your-github-username

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

It motivates me to build and share more projects!

---

## 📄 License

This project is licensed under the MIT License.
