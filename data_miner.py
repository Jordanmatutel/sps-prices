import pandas as pd
from bs4 import BeautifulSoup
import requests
import statistics


def data_creator():
    # This variables saves the recollected data.
    main_price = []
    main_land = []
    m2 = []
    type_of = []
    main_address = []

    # This loops scraps all the data in the page of novacasahn.com.
    for r in range(20):
        try:
            recollected_price = []
            recollected_land = []
            recollected_address = []

            url = f"https://novacasahn.com/city/san-pedro-sula/page/{r}/"
            page = requests.get(url)
            soup = BeautifulSoup(page.content, "html.parser")
            target = soup.find_all("div", class_="item-wrap item-wrap-v1 item-wrap-no-frame h-100")

            # Search for the data
            for i in target:
                types = i.find("li", class_="h-type")
                price = i.find("li", class_="item-price")
                land = i.find("li", class_="h-area")
                land_lote = i.find("li", class_="h-land-area")
                address = i.find("address", class_="item-address")

                c = types.text
                c = c.split("/")[0]
                c = c.split(",")[0]

                if c == "Casas" or c == "Apartamentos" or c == "Townhouses":
                    recollected_price.append(price.text)
                    recollected_address.append(address.text)
                    recollected_land.append(land.text)
                    type_of.append(c)
                elif c == "Lote":
                    recollected_price.append(price.text)
                    recollected_address.append(address.text)
                    recollected_land.append(land_lote.text)
                    type_of.append(c)

            # Makes the price into a numeric function and fix the error in the recollected data.
            price = []
            # Makes the price into a numeric function.
            for i in range(len(recollected_price)):
                recollected_price[i] = recollected_price[i].replace("$", "").replace(".", "").replace(",", "")
                recollected_price[i] = recollected_price[i].split("/")[0]
                if recollected_price[i][0] == "L":
                    recollected_price[i] = recollected_price[i].replace("L", "")
                    recollected_price[i] = float(recollected_price[i])
                    recollected_price[i] = recollected_price[i] * 0.041
                    recollected_price[i] = round(recollected_price[i], 2)
                recollected_price[i] = float(recollected_price[i])
                price.append(recollected_price[i])

            # Fix the error with the recollected data of the area.
            final_land = []
            for i in range(len(recollected_land)):
                recollected_land[i] = recollected_land[i].split(" ")[0]
                recollected_land[i] = float(recollected_land[i])
                if recollected_land[i] > 10:
                    final_land.append(recollected_land[i])

            # Fix the error with the recollected data of the address
            for i in range(len(recollected_address)):
                recollected_address[i] = recollected_address[i].split(",")[0]

            # Calculate the mean price for m2
            mean_m2 = []
            for i in range(len(final_land)):
                c = price[i] / final_land[i]
                c = round(c, 2)
                mean_m2.append(c)

            # Save the data into the principal variables
            main_price = main_price + price
            main_land = main_land + final_land
            main_address = main_address + recollected_address
            m2 = m2 + mean_m2

        finally:
            pass

    # Calculate the Standard Deviation of the price
    mean = sum(main_price) / len(main_price)
    sdt = statistics.stdev(main_price)
    negative_sdt = mean - sdt
    double_sdt = (sdt * 2) + mean
    dnegative_sdt = mean - (negative_sdt * 2)
    sdt = mean + sdt

    # Classify the data in base of the standard deviation
    total_list = []
    for i in range(len(main_price)):
        if main_price[i] > sdt:
            if main_price[i] > double_sdt:
                total_list.append("Very High Price")
            else:
                total_list.append("High Price")
        elif main_price[i] < negative_sdt:
            if main_price[i] < dnegative_sdt:
                total_list.append("Very Low Price")
            else:
                total_list.append("Low Price")
        else:
            total_list.append("Medium Price")

    # Creates the dataframe and save it in one .csv
    data = pd.DataFrame(columns=["Price", "Land", "Area", "Type", "m2 price", "Price Value"])
    data["Price"] = main_price
    data["Land"] = main_land
    data["Area"] = main_address
    data["Type"] = type_of
    data["m2 price"] = m2
    data["Price Value"] = total_list

    data = data.sort_values(by='Area')

    # Delete the duplicate rows
    for index, row in data.iterrows():
        if data.loc[(data['Price'] == row['Price']) & (data['Land'] == row['Land'])].shape[0] > 1:
            data = data.drop(index)

    data.to_csv("Data.csv", index=False)
