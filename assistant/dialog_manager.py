def ask_for_additional_details(intent, user_input):
    if intent == "weather_ambiguous":
        return "Could you please tell me your location (city or country)?" #Not working
    elif intent == "web_scrape":
        return "Could you clarify the subject? Do you mean a specific person or topic?"
    else:
        return "Sorry, I need more details for this query."