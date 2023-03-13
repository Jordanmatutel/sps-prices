import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def prediction():
    # Import the data
    data = pd.read_csv("Mean Price in Area.csv")
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
        e = (price[i] - predict[i]) ** 2
        e = np.sqrt(e)
        e = round(e, 2)
        error.append(e)

    # Creates the second model, using one lineal regression.
    coefficient = np.polyfit(land, price, 2)
    model2 = []
    for i in range(len(land)):
        m = coefficient[0]
        m2 = coefficient[1]
        b = coefficient[2]
        r = (land[i] * m) + (land[i] * m2) + b
        r = round(r, 2)
        model2.append(r)

    # Calculate the error of our model.
    error2 = []
    for i in range(len(land)):
        e = (price[i] - model2[i]) ** 2
        e = np.sqrt(e)
        e = round(e, 2)
        error2.append(e)

    # Choose between the two models. The model with less error with be the selected.
    if sum(error) > sum(error2):
        result = model2
        error_result = error2
    else:
        result = predict
        error_result = error

    # Saves the information into one archive .csv.
    c = pd.DataFrame({"Price": price, "Land": land, "Area": address, "Predict": result, "Error": error_result})
    c.to_csv("Model Prediction.csv")

    # Graph the results
    price = sorted(price)
    result = sorted(result)
    fig, ax = plt.subplots()
    ax.plot(price, 'o', label='Prices')
    ax.plot(result, '-', label='Prediction')
    ax.set_xlabel('Price')
    ax.set_title('Prices vs Prediction')
    ax.legend()
    plt.show()
