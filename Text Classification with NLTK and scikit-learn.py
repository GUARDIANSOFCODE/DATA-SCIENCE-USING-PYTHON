# Import required libraries
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Download necessary NLTK data files
nltk.download('punkt')
nltk.download('stopwords')

# Sample dataset: Text data and labels
texts = [
    "I love this movie, it was fantastic and thrilling!",
    "This film was terrible, I didn't enjoy it at all.",
    "Amazing performance by the actors, thoroughly enjoyed!",
    "Worst movie ever, completely waste of time.",
    "Brilliant story and great direction.",
    "The movie was okay, but could have been better.",
    "I am never watching this movie again!",
    "Such a wonderful experience, I highly recommend it.",
]
labels = ['positive', 'negative', 'positive', 'negative', 'positive', 'negative', 'negative', 'positive']

# Text preprocessing function
def preprocess_text(text):
    # Tokenize and remove stop words
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text.lower())
    filtered_tokens = [word for word in tokens if word.isalnum() and word not in stop_words]
    return ' '.join(filtered_tokens)

# Preprocess each text in the dataset
processed_texts = [preprocess_text(text) for text in texts]

# Convert text data to feature vectors using CountVectorizer
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(processed_texts)
y = labels

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train the Naive Bayes classifier
classifier = MultinomialNB()
classifier.fit(X_train, y_train)

# Make predictions on the test set
y_pred = classifier.predict(X_test)

# Evaluate the classifier
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
