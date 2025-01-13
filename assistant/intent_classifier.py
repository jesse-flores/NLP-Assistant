from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

#EXPAND
training_sentences = ["What's the weather like?", "Tell me a joke", "What time is it?"]
training_labels = ["weather", "joke", "time"]

vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(training_sentences)
classifier = MultinomialNB()
classifier.fit(X_train, training_labels)

def classify_intent(text):
    X_test = vectorizer.transform([text])
    return classifier.predict(X_test)[0]