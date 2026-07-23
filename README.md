# 🛍️ Product Review Analysis & Smart Recommendation System

An AI-powered web application that analyzes customer reviews, predicts their sentiment, and recommends relevant products using Machine Learning and Natural Language Processing (NLP).

🌐 **Live Demo:** https://sandhya57.pythonanywhere.com/

💻 **GitHub Repository:** https://github.com/sandhya5796/Product-Review-Analysis-System

---

# 📌 Project Overview

The **Product Review Analysis & Smart Recommendation System** is a Flask-based web application that helps users understand customer opinions and discover relevant products.

The application uses **Support Vector Machine (SVM)** for sentiment classification and **TF-IDF with Cosine Similarity** for product recommendations.

Users can enter a product review, and the application predicts whether the sentiment is **Positive**, **Neutral**, or **Negative** while suggesting similar products based on review content.

---

# ✨ Features

- 🔍 Customer Review Sentiment Analysis
- 😊 Sentiment Prediction (Positive, Neutral, Negative)
- 🤖 Smart Product Recommendation System
- 📊 Machine Learning-based Prediction
- ⚡ Fast Review Processing
- 🌐 Flask Web Application
- 📱 Responsive User Interface
- 🎯 Personalized Product Suggestions

---

# 🛠️ Tech Stack

## Programming Language

- Python

## Machine Learning

- Scikit-learn
- Support Vector Machine (SVM)
- TF-IDF Vectorizer
- Cosine Similarity
- Pandas
- NumPy

## Web Development

- Flask
- HTML5
- CSS3
- JavaScript

## Tools

- Git
- GitHub
- VS Code
- Google Colab
- Jupyter Notebook

---

# 📂 Project Structure

```
Product-Review-Analysis-System
│
├── flask_app.py
├── requirements.txt
├── producttttt.csv
├── svm_sentiment_modellll.pkl
├── tfidf_vectorizerrrr.pkl
├── recommendtf.pkl
│
├── templates/
│      └── pred.html
│
├── static/
│      ├── css/
│      ├── images/
│      └── js/
│
│
└── README.md
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/sandhya5796/Product-Review-Analysis-System.git
```

---

## 2. Navigate to the Project Folder

```bash
cd Product-Review-Analysis-System
```

---

## 3. Create a Virtual Environment (Optional)

```bash
python -m venv venv
```

---

## 4. Activate the Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## 5. Install Required Libraries

```bash
pip install -r requirements.txt
```

---

## 6. Run the Flask Application

```bash
python flask_app.py
```

---

## 7. Open in Browser

```
http://127.0.0.1:5000
```

Or use the deployed application:

**https://sandhya57.pythonanywhere.com/**

---

# 🚀 How It Works

1. User enters a product review.
2. The review is cleaned and preprocessed.
3. TF-IDF converts the text into numerical features.
4. The trained SVM model predicts the sentiment.
5. Cosine Similarity identifies products with similar reviews.
6. The application displays personalized product recommendations.

---

# 📊 Machine Learning Workflow

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
      SVM Sentiment Classification
                     │
                     ▼
          Cosine Similarity
                     │
                     ▼
      Recommended Products
```

---


---

# 📈 Model Information

| Model | Purpose |
|-------|---------|
| Support Vector Machine (SVM) | Sentiment Classification |
| TF-IDF | Feature Extraction |
| Cosine Similarity | Product Recommendation |

---

# 🎯 Skills Demonstrated

- Python Programming
- Machine Learning
- Natural Language Processing (NLP)
- Flask Web Development
- HTML5 & CSS3
- JavaScript
- REST API Development
- Data Preprocessing
- Feature Engineering
- Git & GitHub
- Software Development
- Debugging
- Problem Solving

---

# 🚀 Future Improvements

- User Authentication
- Database Integration (MySQL)
- Admin Dashboard
- Advanced Recommendation Algorithms
- BERT-based Sentiment Analysis
- Cloud Deployment using AWS/Render
- Real-time Product Reviews
- Product Search Functionality
- Shopping Cart Integration
- Multilingual Review Support

---

# 📚 Dataset

This project is developed using the **Women's E-Commerce Clothing Reviews** dataset from Kaggle.

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Push the branch.
5. Create a Pull Request.

---

# 👩‍💻 Author

**Eedupuganti Divya Sai Sandhya**

🎓 B.Tech – Computer Science and Engineering (IoT & Cyber Security including Blockchain)

🏫 Sasi Institute of Technology and Engineering

💼 LinkedIn:
https://www.linkedin.com/in/your-linkedin-profile

💻 GitHub:
https://github.com/sandhya5796

🌐 Live Demo:
https://sandhya57.pythonanywhere.com/

---

# ⭐ Show Your Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

Your support motivates me to build and share more projects.

---

# 📄 License

This project is licensed under the **MIT License**.

Feel free to use, modify, and distribute this project for educational and learning purposes.
