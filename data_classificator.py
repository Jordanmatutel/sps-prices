import pandas as pd
import statistics as st


def processor():
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
    total_list = []
    for i in range(len(price)):
        if area[i] >= sdt:
            if area[i] >= double_sdt:
                total_list.append("Very High Price")
            else:
                total_list.append("High Price")
        if area[i] <= negative_sdt:
            if area[i] >= dnegative_sdt:
                total_list.append("Very Low Price")
            else:
                total_list.append("Low Price")
        else:
            total_list.append("Medium Price")

    return total_list
