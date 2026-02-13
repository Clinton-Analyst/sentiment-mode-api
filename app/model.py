from textblob import TextBlob
from collections import Counter

def analyze_sentiment(text: str):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return {
        "sentiment": sentiment,
        "polarity": polarity
    }


def calculate_mode(sentiments: list):
    counter = Counter(sentiments)
    return counter.most_common(1)[0][0]
