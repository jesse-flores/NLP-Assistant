from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    sentiment_score = analyzer.polarity_scores(text)
    if sentiment_score['compound'] >= 0.08:
        return "positive"
    elif sentiment_score['compound'] <= -0.08:
        return "negative"
    else:
        return "neutral"