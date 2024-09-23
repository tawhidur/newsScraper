from linecache import clearcache
import time
import requests
from bs4 import BeautifulSoup
from collections import Counter
import re

clearcache()


# General function to scrape headlines from a website with multiple tag options
def scrape_headlines(url, headline_tags):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')

        headlines = []
        for tag in headline_tags:
            headlines += soup.find_all(tag)
        return [headline.get_text(strip=True) for headline in headlines]
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return []


# Function to scrape Prothom Alo
def scrape_prothom_alo():
    return {'Prothom Alo': scrape_headlines("https://en.prothomalo.com/", ['h2', 'h3', 'h1', 'h4'])}


# Function to scrape The Daily Star
def scrape_daily_star():
    return {'The Daily Star': scrape_headlines("https://www.thedailystar.net", ['h3', 'h2', 'h4', 'h1'])}


# Function to scrape Dhaka Tribune
def scrape_dhaka_tribune():
    return {'Dhaka Tribune': scrape_headlines("https://www.dhakatribune.com", ['h3', 'h2', 'h1', 'h4'])}


# Function to scrape The Financial Express
def scrape_financial_express():
    return {
        'The Financial Express': scrape_headlines("https://www.thefinancialexpress.com.bd", ['h2', 'h1', 'h3', 'h4'])}


# Function to scrape The Business Standard
def scrape_business_standard():
    return {'The Business Standard': scrape_headlines("https://www.tbsnews.net", ['h3', 'h2', 'h1', 'h4'])}


# Function to scrape Bangladesh Post
def scrape_bangladesh_post():
    return {'Bangladesh Post': scrape_headlines("https://www.bangladeshpost.net", ['h3', 'h2', 'h1', 'h4'])}


# Function to scrape BD News 24
def scrape_bdnews24():
    return {'BD News 24': scrape_headlines("https://bdnews24.com/", ['h2', 'h1', 'h3', 'h4'])}


# Filter headlines for specific keywords
def filter_headlines_by_keywords(headlines, keywords):
    pattern = re.compile('|'.join(keywords), re.IGNORECASE)
    return {source: [headline for headline in headline_list if pattern.search(headline)] for source, headline_list in
            headlines.items()}


# Analyze headlines to show a summary
def analyze_headlines(filtered_headlines):
    word_counter = Counter([headline for headlines in filtered_headlines.values() for headline in headlines])
    return word_counter.most_common()


# Generate and display the summary report
def generate_report():
    print("Scraping headlines from multiple Bangladeshi news sources...\n")

    # Wait time between each scraping
    wait_time = 5

    # Scrape headlines from each source
    all_headlines = {}
    sources = [
        scrape_prothom_alo,
        scrape_daily_star,
        scrape_dhaka_tribune,
        scrape_financial_express,
        scrape_business_standard,
        scrape_bangladesh_post,
        scrape_bdnews24
    ]

    for source in sources:
        all_headlines.update(source())
        time.sleep(wait_time)  # Adding wait time

    # Filter headlines by specific keywords
    keywords = ['BNP', 'Bangladesh Nationalist Party', 'Nationalist', 'bnp', 'Begum Khaleda Zia', 'Khaleda Zia',
                'Tarique Rahman', 'Tarique', 'Tarique', 'antibnp']
    filtered_headlines = filter_headlines_by_keywords(all_headlines, keywords)

    # Display filtered headlines grouped by source
    print("Filtered Headlines:\n")
    for source, headlines in filtered_headlines.items():
        if headlines:
            print(f"\nSource: {source}")
            for headline in headlines:
                print(f" - {headline}")

    # Display summary
    print("\nSummary of Today's Filtered Headlines:\n")
    common_topics = analyze_headlines(filtered_headlines)
    for topic, count in common_topics:
        print(f" - '{topic}' appeared {count} times")


# Run the summary report
generate_report()
