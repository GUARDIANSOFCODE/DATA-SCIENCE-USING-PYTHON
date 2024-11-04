import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download VADER lexicon if not already downloaded
nltk.download('vader_lexicon')

def analyze_sentiment(text):
    # Initialize the VADER sentiment intensity analyzer
    sia = SentimentIntensityAnalyzer()
    
    # Get sentiment scores
    sentiment_scores = sia.polarity_scores(text)
    
    return sentiment_scores

if __name__ == "__main__":
    text = "I love programming in Python! It's so much fun and powerful."
    scores = analyze_sentiment(text)
    print(f"Sentiment Scores: {scores}")
