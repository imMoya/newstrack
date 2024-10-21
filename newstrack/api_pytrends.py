from pytrends.request import TrendReq
import pandas as pd

def get_trending_data(keywords, timeframe='today 5-y', geo=''):
    """
    Fetch Google Trends data for the specified keywords.

    Args:
        keywords (list): A list of search terms.
        timeframe (str): Timeframe for the data (e.g., 'today 5-y', 'now 7-d'). Default is 'today 5-y'.
        geo (str): The geographical area for the data (e.g., 'US' for the United States). Default is global.

    Returns:
        pd.DataFrame: A DataFrame with interest over time for the specified keywords.
    """
    pytrends = TrendReq(hl='en-US', tz=360)
    
    # Build the payload with the given keywords
    pytrends.build_payload(keywords, timeframe=timeframe, geo=geo)

    # Retrieve interest over time
    data = pytrends.interest_over_time()

    if not data.empty:
        # Drop the 'isPartial' column (if present)
        data = data.drop(columns=['isPartial'], errors='ignore')
    
    return data

def get_related_queries(keyword):
    """
    Fetch related queries for a specific keyword.

    Args:
        keyword (str): The search term for which related queries should be fetched.

    Returns:
        dict: A dictionary with related queries for rising and top.
    """
    pytrends = TrendReq(hl='en-US', tz=360)
    
    # Build the payload with the given keyword
    pytrends.build_payload([keyword])

    # Get related queries
    related_queries = pytrends.related_queries()
    
    return related_queries.get(keyword, {})