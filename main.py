from assistant import stt, nlu, tts, sentiment, memory, webscrapper, dialog_manager

def main():
    print("Assistant is ready...")

    while True:
        # Listen for speech input
        user_input = stt.listen_for_command()
        if user_input is None:
            continue
        
        # Analyze sentiment
        user_sentiment = sentiment.analyze_sentiment(user_input)
        
        # Process the text for NLU
        intent = nlu.classify_intent(user_input)
        
        # Handle dynamic query responses and ambiguity
        if intent == "weather_ambiguous":
            # Ask the user for location (clarify the query)
            clarification = dialog_manager.ask_for_additional_details(intent, user_input)
            print(clarification)
            tts.speak(clarification)
            # Listen for the location response
            location = stt.listen_for_command()
            if location:
                response = webscrapper.web_scrape_weather(location)
            else:
                response = "I couldn't get your location, sorry."
        
        elif intent == "weather":
            # Normal weather query with location specified
            location = user_input.split("in")[-1].strip()  # Extract location from query
            response = webscrapper.web_scrape_weather(location)
        
        elif intent == "web_scrape":
            subject = user_input.split("who is")[-1].strip()  # Basic extraction
            response = webscrapper.web_scrape_wikipedia(subject)
        
        else:
            response = "Sorry, I didn't understand that."

        # Adjust response based on sentiment
        if user_sentiment == "positive":
            response = f"I'm glad you're feeling good! {response}"
        elif user_sentiment == "negative":
            response = f"I'm sorry to hear that. {response}"

        # Speak the response
        tts.speak(response)

if __name__ == "__main__":
    main()