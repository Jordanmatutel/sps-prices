import pandas as pd
import numpy as np
import statistics as st

def proccesor():
    data = pd.read_csv("Data.csv")
    price = data["Price"]
    land = data["Land"]
    area = data["Area"]

