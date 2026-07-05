import nltk
import string
from collections import Counter
import matplotlib.pyplot as plt

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

# -------------------------------
# Read Article
# -------------------------------
with open("article.txt", "r", encoding="utf-8") as file:
    article = file.read()

print("=" * 60)
print("Original Article Length:", len(article.split()), "words")
print("=" * 60)

# -------------------------------
# Tokenization
# -------------------------------
tokens = word_tokenize(article.lower())

print("\nFirst 20 Tokens:")
print(tokens[:20])

# -------------------------------
# Remove Punctuation
# -------------------------------
tokens = [word for word in tokens if word.isalpha()]

# -------------------------------
# Remove Stopwords
# -------------------------------
stop_words = set(stopwords.words("english"))

filtered_words = [
    word for word in tokens
    if word not in stop_words
]

print("\nWords after removing stopwords:", len(filtered_words))

# -------------------------------
# Stemming
# -------------------------------
stemmer = PorterStemmer()

stemmed_words = [
    stemmer.stem(word)
    for word in filtered_words
]

# -------------------------------
# Lemmatization
# -------------------------------
lemmatizer = WordNetLemmatizer()

lemmatized_words = [
    lemmatizer.lemmatize(word)
    for word in filtered_words
]

print("\nSample Stemmed Words:")
print(stemmed_words[:20])

print("\nSample Lemmatized Words:")
print(lemmatized_words[:20])

# -------------------------------
# Keyword Extraction
# -------------------------------
word_counts = Counter(lemmatized_words)

top_keywords = word_counts.most_common(15)

print("\nTop 15 Keywords")
print("-" * 40)

for word, count in top_keywords:
    print(f"{word:15} {count}")

# -------------------------------
# Most Frequent Words
# -------------------------------
top10 = word_counts.most_common(10)

words = [item[0] for item in top10]
counts = [item[1] for item in top10]

print("\nMost Frequent Words")
print("-" * 40)

for word, count in top10:
    print(f"{word:15} {count}")

# -------------------------------
# Visualization
# -------------------------------
plt.figure(figsize=(10,5))
plt.bar(words, counts)

plt.title("Top 10 Most Frequent Words")
plt.xlabel("Words")
plt.ylabel("Frequency")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
