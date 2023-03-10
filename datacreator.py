import pandas as pd
from bs4 import BeautifulSoup
import requests

# This variables saves the recollected data.
main_price = []
main_land = []
main_address = []

# This loops
for r in range(3):
    try:
        url = f"https://novacasahn.com/city/san-pedro-sula/page/{r}/"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")

        # Prices
        price = soup.find_all("li", class_="item-price")
        land = soup.find_all("span", class_="hz-figure")
        address = soup.find_all("address", class_="item-address")

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

        # Makes all the size of the variables equal.
        price = price[0:9]
        recollected_address = recollected_address[0:9]

        # Save the data into the principal variables
        main_price = main_price + price
        main_land = main_land + final_land
        main_address = main_address + recollected_address

    except:
        pass


# Creates the DataFrame

print(len(main_price))
print(len(main_land))
print(len(main_address))


data = pd.DataFrame(columns=["Price", "Land", "Area"])
data["Price"] = main_price
data["Land"] = main_land
data["Area"] = main_address
data.to_csv("Data.csv")
