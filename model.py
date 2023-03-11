import numpy as np
import pandas as pd

def model():
    data = pd.read_csv("Mean_Price_in_Area.csv")
    areas = data["Name of Area"]
    mean_area = data["Mean Area"]
    mean_m2 = data["Mean m2 price"]
    data = pd.read_csv("Data.csv")
    price = data["Price"]
    land = data["Land"]
    address = data["Area"]

