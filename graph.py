import pandas as pd
import matplotlib.pyplot as plt
import math


def graph():
    # Reads the data and take the unique values and counts them.
    data = pd.read_csv("All prices in Cortes.csv")
    dprices = data["Prices"]
    value_counts = data["Classification"].value_counts()
    categories = data["Classification"].unique()
    counts = [value_counts[cat] for cat in categories]
    mean = data["Prices"].mean()
    mean = round(mean, 2)

    # Reads the data from the second study.
    data2 = pd.read_csv("Data.csv")
    total = len(data2["Price"])
    value_count2 = data2["Area"].unique()
    mean2 = data2["Price"].mean()
    mean2 = round(mean2, 2)

    # Reads the data from the model of prediction.
    c = pd.read_csv("Model Prediction.csv")
    error = c["Error"]
    rmse = error ** 2
    rmse = sum(rmse) / len(rmse)
    rmse = math.sqrt(rmse)
    rmse = round(rmse, 2)

    # Writes the results into the readme.txt
    c = f"This study use web scraping in order to get the data from the main sellers of real estate " \
        f"in order to get the major amount of possible data. " \
        f"The study have the values of {len(dprices)} properties ubicated in Cortes, Honduras. The mean price of " \
        f"the properties is {mean}. From this study we take out the registered data from San Pedro Sula which have " \
        f"brings as a result the amount of {total} houses. With this information we divide the " \
        f"quantity of data in base of the regions. In this study I call region to every colony " \
        f"colonies, residential or sector of San Pedro Sula. The amounts of registered regions " \
        f"is {len(value_count2)}. Using this set of data, I take the mean price of the data, " \
        f"that's equal to: {mean2} and divided the properties based on the price. " \
        f"After that, I created two models, one using linear regression and another using the mean " \
        f"price of every area. I set a option tree that return the best option from this case. " \
        f"The best adapted model in this case has a RMSE of {rmse}."

    # Write the output data of the research to the file
    with open("readme.txt", "w") as f:
        f.write(str(c))

