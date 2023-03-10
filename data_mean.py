import pandas as pd


def mean_price_area():
    # Reads the saved data.
    data = pd.read_csv("Data.csv")

    # Get a list of unique areas.
    areas = data["Area"].unique()

    # Calculate the mean price for each area.
    mean_area_price = []
    for area in areas:
        prices = data[data["Area"] == area]["Price"]
        mean_price = prices.mean()
        mean_price = round(mean_price, 2)
        mean_area_price.append(mean_price)

    # Calculate the mean price of m2 of land.
    mean_m2 = []
    for area in areas:
        prices = data[data["Area"] == area]["m2 price"]
        mean_price = prices.mean()
        mean_price = round(mean_price, 2)
        mean_m2.append(mean_price)

    # Difference from the mean price of area.
    all_mean = data["Price"].mean()
    all_mean = round(all_mean, 2)
    difference = []
    for i in range(len(mean_area_price)):
        c = all_mean - mean_area_price[i]
        c = round(c, 2)
        difference.append(c)

    # Percentage that represents the difference with the mean price and the difference.
    variance = []
    for i in range(len(mean_area_price)):
        c = difference[i] / all_mean
        c = round(c, 4)
        variance.append(c)

    # Create the CSV file with the mean price for each area.
    total = pd.DataFrame(columns=["Name of Area", "Mean Area", "Mean m2 price",
                                  "Mean Area - Total Mean", "Variance"])
    total["Name of Area"] = areas
    total["Mean Area"] = mean_area_price
    total["Mean m2 price"] = mean_m2
    total["Mean Area - Total Mean"] = difference
    total["Variance"] = variance
    total.to_csv("Mean Price in Area.csv", index=False)
