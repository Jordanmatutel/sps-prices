import numpy as np
import pandas as pd

def model():
    data = pd.read_csv("Mean_Price_in_Area.csv")
    areas = data["Name of Area"]
    mean_area = data["Mean Area"]
    data = pd.read_csv("Data.csv")
    land = data["Land"]
    address = data["Area"]

    for i in range(len(land)):
        


