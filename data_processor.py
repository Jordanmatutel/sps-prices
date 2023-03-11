import pandas as pd
import numpy as np
import statistics as st

def proccesor():
    data = pd.read_csv("Data.csv")
    price = data["Price"]
    land = data["Land"]
    area = data["Area"]

    # Calculate the Standard Deviation of the price
    sdt = st.stdev(price)
    negative_sdt = -sdt
    double_sdt = sdt * 2
    dnegative_sdt = negative_sdt * 2

    # Classify the data in base of the standard deviation
    list = []
    numerical_list = []
    for i in range(len(price)):
        if area[i] >= sdt:
            if area[i] >= double_sdt:
                list.append("Very High Price")
            else:
                list.append("High Price")
        if area[i] <= negative_sdt:
            if area[i] >= dnegative_sdt:
                list.append("Very Low Price")
            else:
                list.append("Low Price")
        else:
            list.append("Medium Price")

