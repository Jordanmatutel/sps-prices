import pandas as pd


def mean_price_area():
    # Reads the saved data.
    data = pd.read_csv("Data.csv")
    price = data["Price"]
    area = data["Area"]

    # This loops classify the areas and then it takes the mean.
    a = "A"
    areas = []
    for i in range(len(area)):
        if area[i] != a:
            areas.append(area[i])
            a = area[i]

    # Adds the mean price for every area.
    c = []
    mean = []
    # For every area, the variable of area its compared to the variable of areas.
    # If they're the same, it counts the total prices and return the mean price of the area.
    for i in range(len(areas)):
        for j in range(len(area)):
            if area[j] == area[i]:
                c.append(price[j])
            if area[j] != area[i]:
                if len(c) > 0:
                    r = sum(c) / len(c)
                    mean.append(r)
                c = []

    # Creates the archive .csv with mean price of every area.
    c = pd.DataFrame(columns=["Name of Area", "Mean Price"])
    c["Name of Area"] = areas
    c["Mean Price"] = mean
    c.to_csv("Mean_Price_in_Area.csv")
