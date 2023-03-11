import pandas as pd


def mean_price_area():
    # Reads the saved data.
    data = pd.read_csv("Data.csv")

    # Get a list of unique areas.
    areas = data["Area"].unique().tolist()

    # Calculate the mean price for each area.
    mean_area_price = data.groupby("Area")["Price"].mean()

    # Difference from the mean price of area.
    all_mean = data["Price"].mean()
    all_mean = round(all_mean, 2)
    difference = []
    for i in range(len(mean_area_price)):
        c = mean_area_price[i] - all_mean
        c = round(c, 2)
        difference.append(c)

    # Percentage difference between the mean price and the mean of the area.
    weight = []
    for i in range(len(mean_area_price)):
        c = difference[i] / all_mean
        c = round(c, 2)
        weight.append(c)

    # Create the CSV file with the mean price for each area.
    df = pd.DataFrame({"Name of Area": areas, "Mean Area": mean_area_price,
                       "Total Mean - Mean Area": difference, "%": weight})

    df.to_csv("Mean_Price_in_Area.csv", index=False)
