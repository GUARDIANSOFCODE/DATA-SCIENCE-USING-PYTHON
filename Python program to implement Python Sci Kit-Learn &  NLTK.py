# Importing necessary libraries
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Download NLTK data files (first time use)
nltk.download('punkt')
nltk.download('stopwords')

# Sample data (you can replace this with your dataset)
texts = [
    "I love programming in Python.",
    "Python is a versatile language.",
    "I dislike bugs in the code.",
    "Debugging can be very challenging.",
    "Learning Python is fun and rewarding."
]

labels = [1, 1, 0, 0, 1]  # 1 = Positive, 0 = Negative

# Text Preprocessing using NLTK
def preprocess_text(text):
    # Tokenize
    tokens = nltk.word_tokenize(text.lower())
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word.isalnum() and word not in stop_words]
    # Stemming
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(word) for word in tokens]
    return ' '.join(tokens)

# Preprocess all texts
processed_texts = [preprocess_text(text) for text in texts]

# Vectorization using CountVectorizer from scikit-learn
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(processed_texts)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.3, random_state=42)

# Train a Naive Bayes classifier
classifier = MultinomialNB()
classifier.fit(X_train, y_train)

# Make predictions
y_pred = classifier.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f"Accuracy: {accuracy * 100:.2f}%")
print("Classification Report:")
print(report)
