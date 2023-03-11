import pandas as pd
from bs4 import BeautifulSoup
import requests


def data_creator():
    # This variables saves the recollected data.
    main_price = []
    main_land = []
    m2 = []
    main_address = []

    # This loops scraps all the data in the page of novacasahn.com.
    for r in range(3):
        try:
            url = f"https://novacasahn.com/city/san-pedro-sula/page/{r}/"
            page = requests.get(url)
            soup = BeautifulSoup(page.content, "html.parser")
            target = soup.find("div", class_="col-lg-8 col-md-12 bt-content-wrap")

            # Prices
            price = target.find_all("li", class_="item-price")
            land = target.find_all("span", class_="hz-figure")
            address = target.find_all("address", class_="item-address")

            # Take the recollected data an save it.
            recollected_price = []
            recollected_land = []
            recollected_address = []
            for i in price:
                recollected_price.append(i.text)
            for i in land:
                recollected_land.append(i.text)
            for i in address:
                recollected_address.append(i.text)

            # Makes the price into a numeric function.
            price = []
            last_price = 0
            for i in range(len(recollected_price)):
                recollected_price[i] = recollected_price[i].replace("$", "").replace(".", "").replace(",", "")
                recollected_price[i] = recollected_price[i].split("/")[0]
                recollected_price[i] = float(recollected_price[i])
                if recollected_price[i] != last_price:
                    price.append(recollected_price[i])
                last_price = recollected_price[i]

            # Fix the error with the recollected data of the area.
            final_land = []
            for i in range(len(recollected_land)):
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

    # Creates the dataframe and save it in one .csv
    data = pd.DataFrame(columns=["Land", "Area", "Price", "m2"])
    data["Price"] = main_price
    data["Land"] = main_land
    data["Area"] = main_address
    data["m2 price"] = m2
    data = data.sort_values(by='Area')
    data.to_csv("Data.csv", index=False)
