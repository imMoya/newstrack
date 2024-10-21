import pandas as pd
from datetime import datetime, timedelta
from .api import find_articles

def store_articles_monthly(search_term, api_key):
    today = datetime.today()
    three_months_ago = today - timedelta(days=90)
    start_date = datetime(three_months_ago.year, three_months_ago.month, 1)
    
    date_range = pd.date_range(start=start_date, end=today, freq='MS')
    article_data = []

    for date in date_range:
        start_str = date.strftime('%Y-%m-%d')
        end_of_month = (date + pd.DateOffset(months=1) - timedelta(days=1)).strftime('%Y-%m-%d')
        articles_found = find_articles(search_term, api_key, start_str, end_of_month)
        article_data.append({
            'month': date.strftime('%Y-%m'),
            'found_articles': articles_found
        })

    df = pd.DataFrame(article_data)
    df.set_index('month', inplace=True)
    
    return df