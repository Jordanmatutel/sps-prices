import pandas as pd
import numpy as np


def prediction():
    data = pd.read_csv("Mean_Price_in_Area.csv")
    areas = data["Name of Area"]
    mean_m2 = data["Mean m2 price"]
    data = pd.read_csv("Data.csv")
    price = data["Price"]
    land = data["Land"]
    address = data["Area"]

    # The model predict the price of the terrain in base of the mean price of the area.
    predict = []
    for i in range(len(address)):
        for j in range(len(areas)):
            if areas[j] == address[i]:
                m2 = mean_m2[j]
                p = m2 * land[i]
                p = round(p, 2)
                predict.append(p)

    # Calculate the error of our model.
    error = []
    for i in range(len(land)):
        e = (land[i] - predict[i]) ** 2
        e = np.sqrt(e)
        e = round(e, 2)
        error.append(e)

    # Saves the information into one archive .csv
    c = pd.DataFrame({"Price": price, "Land": land, "Area": address, "Predict": predict, "Error": error})
    c.to_csv("Model Prediction.csv")
    return predict
