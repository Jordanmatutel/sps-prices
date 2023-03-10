import pandas as pd
from bs4 import BeautifulSoup
import requests

url = "https://novacasahn.com/city/san-pedro-sula/"
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

# Creates the DataFrame
data = pd.DataFrame(columns=["Price", "Land", "Area"])
data["Price"] = price
data["Land"] = final_land
data["Area"] = recollected_address
data.to_csv("Data.csv")
