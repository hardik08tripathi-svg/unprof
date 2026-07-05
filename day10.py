from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ----------------------------------------
# Dataset (5 Documents)
# ----------------------------------------

documents = [
    "Python is a popular programming language used for data science and machine learning.",
    "Artificial Intelligence and Machine Learning are transforming modern technology.",
    "Web development uses HTML, CSS, JavaScript, and Python frameworks like Django.",
    "Data Science includes statistics, data visualization, machine learning, and Python.",
    "Cybersecurity protects computer systems and networks from cyber attacks."
]

# ----------------------------------------
# Display Documents
# ----------------------------------------

print("Available Documents:\n")

for i, doc in enumerate(documents, start=1):
    print(f"Document {i}:")
    print(doc)
    print()

# ----------------------------------------
# User Query
# ----------------------------------------

query = input("\nEnter your search query: ")

# ----------------------------------------
# Bag of Words
# ----------------------------------------

bow_vectorizer = CountVectorizer()

bow_matrix = bow_vectorizer.fit_transform(documents)

query_bow = bow_vectorizer.transform([query])

bow_similarity = cosine_similarity(query_bow, bow_matrix)

# ----------------------------------------
# TF-IDF
# ----------------------------------------

tfidf_vectorizer = TfidfVectorizer()

tfidf_matrix = tfidf_vectorizer.fit_transform(documents)

query_tfidf = tfidf_vectorizer.transform([query])

tfidf_similarity = cosine_similarity(query_tfidf, tfidf_matrix)

# ----------------------------------------
# Results
# ----------------------------------------

print("\nBag of Words Similarity Scores")

for i, score in enumerate(bow_similarity[0]):
    print(f"Document {i+1}: {score:.3f}")

print("\nTF-IDF Similarity Scores")

for i, score in enumerate(tfidf_similarity[0]):
    print(f"Document {i+1}: {score:.3f}")

# ----------------------------------------
# Best Match
# ----------------------------------------

best_match = tfidf_similarity.argmax()

print("\n" + "="*50)
print("Most Similar Document")
print("="*50)

print(f"\nDocument {best_match+1}:")
print(documents[best_match])

print(f"\nSimilarity Score: {tfidf_similarity[0][best_match]:.3f}")
