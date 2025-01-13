import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

def classify_intent(text):
    if "weather" in text:
        # Check if location is mentioned in the text (basic check)
        if "in" not in text and "at" not in text:
            return "weather_ambiguous"  # Flag as ambiguous weather query
        return "weather"
    elif "who is" in text or "tell me about" in text:
        return "web_scrape"
    else:
        return "generic_search"