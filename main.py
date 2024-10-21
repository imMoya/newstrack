from newstrack import load_api_key, store_articles_monthly, plot_article_data
from newstrack.api_pytrends import get_trending_data, get_related_queries
import matplotlib.pyplot as plt
import pandas as pd

if __name__ == "__main__":
    api_key = load_api_key()
    df = store_articles_monthly("lng papua", api_key)
    plot_article_data(df, figfolder="figs")
    keywords = ["lng papua"]
    df = get_trending_data(keywords)
    df.index = pd.to_datetime(df.index)  # Ensure the index is in DateTime format

    # Group by month and sum the 'lng' column
    monthly_totals = df.resample('M').sum()

    print(monthly_totals)
    # Plot the trends data
    if not monthly_totals.empty:
        monthly_totals.tail(4).plot(kind='bar', figsize=(10, 5))
        plt.title('Google Trends Over Time')
        plt.ylabel('Interest Over Time')
        plt.xlabel('Date')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()