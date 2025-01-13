import requests
from bs4 import BeautifulSoup

def web_scrape_weather(location):
    """Scrape weather information from a weather website."""
    # Replace with actual API query or scraping logic
    url = f"https://www.weather.com/weather/today/l/{location.replace(' ', '+')}"
    
    try:
        response = requests.get(url)
        if response.status_code != 200:
            return "Sorry, I couldn't find weather information for that location."
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        temperature = soup.find('span', class_='CurrentConditions--tempValue--3KcTQ').text
        condition = soup.find('div', class_='CurrentConditions--phraseValue--2xXSr').text
        
        return f"The current weather in {location} is {temperature} with {condition}."
    
    except Exception as e:
        return f"Error while scraping weather data: {e}"

def web_scrape_wikipedia(query):
    """Scrape Wikipedia for a given query."""
    url = f"https://en.wikipedia.org/wiki/{query.replace(' ', '_')}"
    
    try:
        response = requests.get(url)
        if response.status_code != 200:
            return "Sorry, I couldn't find any information on that topic."
        
        soup = BeautifulSoup(response.content, 'html.parser')
        paragraphs = soup.find_all('p')
        
        first_paragraph = paragraphs[0].get_text()
        return first_paragraph
    except Exception as e:
        return f"Error while scraping Wikipedia: {e}"