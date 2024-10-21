from newstrack import load_api_key, store_articles_monthly, plot_article_data

if __name__ == "__main__":
    api_key = load_api_key()
    df = store_articles_monthly("lng + png", api_key)
    plot_article_data(df, figfolder="figs")