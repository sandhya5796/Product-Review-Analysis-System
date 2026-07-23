from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import pickle
import re
import string
from sklearn.metrics.pairwise import cosine_similarity


app = Flask(__name__)


# ==============================
# LOAD MODELS
# ==============================

model = pickle.load(
    open("/home/sandhya57/mysite/svm_sentiment_modellll.pkl", "rb")
)

tfidf = pickle.load(
    open("/home/sandhya57/mysite/tfidf_vectorizerrrr.pkl", "rb")
)

recommend_tfidf = pickle.load(
    open("/home/sandhya57/mysite/recommendtf.pkl", "rb")
)


# ==============================
# LOAD DATA
# ==============================

product_df = pd.read_csv(
    "/home/sandhya57/mysite/productttt.csv"
)

# Recommendation matrix
recommend_matrix = recommend_tfidf.transform(product_df["Clean_Text"])

# Feature names, cached once (used to explain matches)
FEATURE_NAMES = np.array(recommend_tfidf.get_feature_names_out())


def fallback_title(row):
    """
    Some rows in the catalog have no Title. Rather than printing the
    literal string "nan", fall back to a short auto-generated title
    built from the review text so every card has something readable.
    """
    title = row.get("Title")
    if pd.notna(title) and str(title).strip().lower() not in ("", "nan"):
        return str(title).strip()

    text = str(row.get("Review Text", "")).strip()
    if text and text.lower() != "nan":
        words = text.split()
        short = " ".join(words[:6])
        return short + ("…" if len(words) > 6 else "")

    return "Unnamed product"


product_df["Display_Title"] = product_df.apply(fallback_title, axis=1)


def get_trending_products(n=6):
    """
    A static preview of the catalog's best-rated products, shown on the
    homepage so the page has real content before anyone submits a review —
    the same way a real storefront shows products before you search.
    """
    df = product_df.copy()
    df["Rating"] = pd.to_numeric(df["Rating"], errors="coerce")
    df = df.dropna(subset=["Rating"])
    df = df.drop_duplicates(subset=["Display_Title"])
    df = df.sort_values("Rating", ascending=False)
    return df.head(n)[["Display_Title", "Rating", "Review Text"]].values.tolist()


TRENDING_PRODUCTS = get_trending_products()

# A small stoplist of generic words that aren't useful as an "explanation"
# even though they can carry tf-idf weight (tune this list to your data).
GENERIC_WORDS = {
    "product", "item", "amazon", "review", "bought", "would", "really",
    "one", "get", "got", "use", "used", "using",
}


# ==============================
# TEXT CLEANING
# ==============================

def clean_text(text):
    text = str(text)
    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"\d+", "", text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = re.sub(r"\s+", " ", text).strip()
    return text


# ==============================
# SENTIMENT FUNCTION
# ==============================

def predict_sentiment(review):
    cleaned = clean_text(review)
    vector = tfidf.transform([cleaned])
    prediction = model.predict(vector)[0]

    if prediction == "Positive":
        return "Positive 😊"
    elif prediction == "Negative":
        return "Negative 😞"
    elif prediction == "Neutral":
        return "Neutral 😐"
    else:
        mapping = {
            0: "Negative 😞",
            1: "Neutral 😐",
            2: "Positive 😊",
        }
        return mapping.get(prediction, str(prediction))


# ==============================
# RECOMMENDATION SYSTEM (with explanations)
# ==============================

def explain_match(user_vector_row, product_vector_row, top_n=4):
    """
    Returns the words that are actually responsible for the similarity
    score between the review and a given product: words present (with
    tf-idf weight) in BOTH the review and the product text, ranked by
    how much they contribute to the match.
    """
    overlap = user_vector_row * product_vector_row
    if overlap.sum() == 0:
        return []

    top_indices = overlap.argsort()[::-1]
    keywords = []
    for i in top_indices:
        if overlap[i] <= 0:
            break
        word = FEATURE_NAMES[i]
        if word in GENERIC_WORDS:
            continue
        keywords.append(word)
        if len(keywords) == top_n:
            break
    return keywords


def recommend_products(review):
    clean_review = clean_text(review)
    user_vector = recommend_tfidf.transform([clean_review])
    user_row = user_vector.toarray()[0]

    similarity = cosine_similarity(user_vector, recommend_matrix)[0]
    indexes = similarity.argsort()[-5:][::-1]

    results = []
    for idx in indexes:
        product_row = recommend_matrix[idx].toarray()[0]
        keywords = explain_match(user_row, product_row)
        score_pct = round(float(similarity[idx]) * 100, 1)

        row = product_df.iloc[idx]

        if keywords:
            if len(keywords) == 1:
                phrase = keywords[0]
            else:
                phrase = ", ".join(keywords[:-1]) + " and " + keywords[-1]
            why = f"Recommended because other reviewers describe it as {phrase}, matching {score_pct}% of your review"
        else:
            why = f"Recommended based on overall similarity to your review ({score_pct}% overlap)"

        results.append([
            row["Display_Title"],
            row["Rating"],
            row["Review Text"],
            why,
        ])

    return results


# ==============================
# HOME PAGE
# ==============================

@app.route("/", methods=["GET", "POST"])
def home():
    sentiment = None
    recommendations = None
    review = ""

    if request.method == "POST":
        review = request.form["review"]
        sentiment = predict_sentiment(review)
        recommendations = recommend_products(review)

    return render_template(
        "pred.html",
        review=review,
        sentiment=sentiment,
        recommendations=recommendations,
        trending=TRENDING_PRODUCTS,
    )


if __name__ == "__main__":
    app.run(debug=True)