import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# Download the stopwords if not already downloaded
nltk.download('stopwords')
from nltk.corpus import stopwords

# Sample data
data = [
    ("I love programming in Python!", "positive"),
    ("I hate bugs and errors.", "negative"),
    ("Coding is challenging but rewarding.", "positive"),
    ("Debugging can be frustrating.", "negative"),
]

# Split data into texts and labels
texts, labels = zip(*data)

# Create a pipeline for vectorization and model
model = make_pipeline(CountVectorizer(stop_words='english'), MultinomialNB())

# Train the model
model.fit(texts, labels)

# Example of prediction
text_to_predict = ["I enjoy solving problems with code."]
predicted = model.predict(text_to_predict)
print(f"Predicted Sentiment: {predicted[0]}")
