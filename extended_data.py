import requests
import pandas as pd
from bs4 import BeautifulSoup
import statistics


def extended():
    # Set a empty list where the data will be saved.
    main_price = []

    for r in range(1, 25):
        try:
            # Takes the URL and download the HTML of the page.
            url = f"https://vipinmo.com/search?id_country=137&id_region=2109&business_type%5B0%5D=for_sale&order_by=created_at&order=desc&page={r}&for_sale=1&for_rent=0&for_temporary_rent=0&for_transfer=0&lax_business_type=1"
            page = requests.get(url)
            soup = BeautifulSoup(page.content, "html.parser")
            target = soup.find_all("div", class_="col-lg-4 col-md-6 mt-2 mb-2")

            # Takes the data and saves the prices.
            p = []
            for i in target:
                prices = i.find_all("div", class_="col-6")
                for price in prices:
                    price_text = price.find("p").get_text()
                    p.append(price_text)

            # Fix the prices and save them as a float variable.
            price = []
            for i in range(len(p)):
                p[i] = p[i].replace("$", "").replace(".", "").replace(",", "").replace("US", "")
                p[i] = p[i].split("/")[0]
                if p[i][0] == "L":
                    p[i] = p[i].replace("L", "")
                    p[i] = float(p[i])
                    p[i] = p[i] * 0.041
                    p[i] = round(p[i], 2)
                p[i] = float(p[i])
                price.append(p[i])

            # Save the data obtained from the loop.
            main_price = main_price + price

        finally:
            pass

    # Import thte data obtained from the data_miner.py and add it to the list.
    c = pd.read_csv("Data.csv")
    new = c["Price"].tolist()
    main_price = main_price + new

    # Takes the mean and the standard deviation of the list.
    mean = sum(main_price) / len(main_price)
    sdt = statistics.stdev(main_price)
    negative_sdt = mean - sdt
    double_sdt = (sdt * 2) + mean
    dnegative_sdt = mean - (negative_sdt * 2)
    sdt = mean + sdt

    # Classify the data using the standard deviation.
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

    # Save the data into one .csv file
    c = pd.DataFrame({"Prices": main_price, "Classification": total_list})
    c.to_csv("All prices in Cortes.csv")
