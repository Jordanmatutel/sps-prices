import pandas as pd
import matplotlib.pyplot as plt


def graph():
    # Reads the data and take the unique values and counts them.
    data = pd.read_csv("Data.csv")
    value_counts = data["Price Value"].value_counts()
    categories = data["Price Value"].unique()
    counts = [value_counts[cat] for cat in categories]

    # Makes the graph of bars and shows it.
    plt.bar(categories, counts)
    plt.show()
