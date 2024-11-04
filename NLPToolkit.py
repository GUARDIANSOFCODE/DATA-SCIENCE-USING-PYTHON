import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import spacy

# Download necessary NLTK data if not already downloaded
nltk.download('vader_lexicon')
nltk.download('stopwords')

# Load the SpaCy NLP model
nlp = spacy.load("en_core_web_sm")

# Function for Sentiment Analysis using NLTK
def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = sia.polarity_scores(text)
    return sentiment_scores

# Function for Named Entity Recognition using SpaCy
def recognize_entities(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

# Function for Text Classification using Scikit-learn and NLTK
def classify_texts(train_data, text_to_predict):
    texts, labels = zip(*train_data)
    model = make_pipeline(CountVectorizer(stop_words='english'), MultinomialNB())
    model.fit(texts, labels)
    predicted = model.predict(text_to_predict)
    return predicted[0]

# Main function to demonstrate all functionalities
def main():
    # Example text for sentiment analysis
    sentiment_text = "I love programming in Python! It's so much fun and powerful."
    sentiment_scores = analyze_sentiment(sentiment_text)
    print(f"Sentiment Scores for '{sentiment_text}': {sentiment_scores}")

    # Example text for named entity recognition
    ner_text = "Apple is looking at buying U.K. startup for $1 billion."
    entities = recognize_entities(ner_text)
    print("Named Entities for the text:")
    for entity in entities:
        print(entity)

    # Sample data for text classification
    train_data = [
        ("I love programming in Python!", "positive"),
        ("I hate bugs and errors.", "negative"),
        ("Coding is challenging but rewarding.", "positive"),
        ("Debugging can be frustrating.", "negative"),
    ]
    
    # Example of text classification
    text_to_predict = ["I enjoy solving problems with code."]
    predicted = classify_texts(train_data, text_to_predict)
    print(f"Predicted Sentiment for '{text_to_predict[0]}': {predicted}")

if __name__ == "__main__":
    main()
