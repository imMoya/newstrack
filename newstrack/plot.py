import os
import pandas as pd
import matplotlib.pyplot as plt

def plot_article_data(df: pd.DataFrame, figfolder=None, filename="plot.png"):
    plt.figure(figsize=(10, 5))
    df['found_articles'].plot(kind='bar', color='skyblue')
    plt.title('Number of Articles Found Over Time')
    plt.xlabel('Month')
    plt.ylabel('Number of Articles')
    plt.xticks(rotation=45)
    plt.tight_layout()

    if figfolder:
        # Ensure the folder exists
        os.makedirs(figfolder, exist_ok=True)
        save_path = os.path.join(figfolder, filename)
        plt.savefig(save_path)
        print(f"Figure saved to {save_path}")
    else:
        plt.show()