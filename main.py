import os
from dotenv import load_dotenv
import json
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import http.client, urllib.parse

# Load API key from environment
def load_api_key():
    load_dotenv()
    return os.getenv("THE_NEWS_API_KEY")

# Make API request and return response data
def find_articles(search_term, api_key, start_date, end_date):
    conn = http.client.HTTPSConnection('api.thenewsapi.com')
    params = urllib.parse.urlencode({
        'api_token': api_key,
        'search': search_term,
        'published_after': start_date,
        'published_before': end_date,
    })
    conn.request('GET', '/v1/news/all?{}'.format(params))
    res = conn.getresponse()
    data = res.read()
    print(data)
    data_str = data.decode('utf-8')
    data_dict = json.loads(data_str)
    found_articles = data_dict['meta']['found']
    conn.close()
    return found_articles

def store_articles_monthly(search_term, api_key):
    today = datetime.today()
    five_years_ago = today - timedelta(days=5*365)  # Approx 5 years
    start_date = datetime(five_years_ago.year, five_years_ago.month, 1)
    
    date_range = pd.date_range(start=start_date, end=today, freq='MS')  # Month start range
    article_data = []

    for date in date_range:
        start_str = date.strftime('%Y-%m-%d')
        end_of_month = (date + pd.DateOffset(months=1) - timedelta(days=1)).strftime('%Y-%m-%d')
        print(start_date)
        print(end_of_month)
        articles_found = find_articles(search_term, api_key, start_str, end_of_month)
        print(articles_found)
        article_data.append({
            'month': date.strftime('%Y-%m'),
            'found_articles': articles_found
        })

    # Convert to DataFrame and set the 'month' as the index
    df = pd.DataFrame(article_data)
    df.set_index('month', inplace=True)
    
    return df

# Extract article timestamps and convert to DataFrame
def extract_article_dates(data):
    articles = data.get('data', [])
    dates = [article['published_at'] for article in articles]
    # Convert to pandas DataFrame and ensure datetime format
    df = pd.DataFrame(dates, columns=['published_at'])
    df['published_at'] = pd.to_datetime(df['published_at'])
    return df

# Group articles by day and count occurrences
def count_articles_per_day(df: pd.DataFrame):
    df.set_index('published_at', inplace=True)
    return df.resample('D').size()  # Resample by day and count articles

# Plot article counts over time
def plot_articles_per_day(article_counts):
    plt.figure(figsize=(10, 6))
    article_counts.plot()
    plt.title('Number of Articles Over Time')
    plt.xlabel('Date')
    plt.ylabel('Number of Articles')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    api_key = load_api_key()
    df = find_articles("lng", api_key, start_date="2024-01-01", end_date="2024-03-01")
    #print(df)
    #df = extract_article_dates(data)
    #article_counts = count_articles_per_day(df)
    #plot_articles_per_day(article_counts)
