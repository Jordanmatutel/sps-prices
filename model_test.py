import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt

# Import the data
data = pd.read_csv("Mean Price in Area.csv")
areas = data["Name of Area"]
mean_m2 = data["Mean m2 price"]
data = pd.read_csv("Data.csv")
price = data["Price"]
land = data["Land"]
address = data["Area"]

# Choose random data using the maximum and the minimum data
# Also selects one random area of the list of areas
random_price = []
mi = min(price)
ma = max(price)
for i in range(1000):
    c = random.randint(mi, ma)
    random_price.append(c)

random_land = []
for i in range(1000):
    c = random.randint(mi, ma)
    random_land.append(c)

random_area = []
for i in range(1000):
    c = random.choice(areas)
    random_area.append(c)


# Creates the first model and return the predict on the data
model1 = []
for i in range(len(random_area)):
    for j in range(len(areas)):
        if random_area[i] == areas[j]:
            m2 = mean_m2[j]
            p = m2 * random_land[i]
            p = round(p, 2)
            model1.append(p)

# Creates the second model, using one linear regression.
linear_regression = np.polyfit(random_land, random_price, 2)
model2 = []
for i in range(len(random_land)):
    m = linear_regression[0]
    m2 = linear_regression[1]
    b = linear_regression[2]
    r = (random_land[i] * m) + (random_land[i] * m2) + b
    r = round(r, 2)
    model2.append(r)

# Calculate the error.
error1 = []
for i in range(len(land)):
    e = (random_price[i] - model1[i]) ** 2
    e = np.sqrt(e)
    e = round(e, 2)
    error1.append(e)

error2 = []
for i in range(len(land)):
    e = (random_price[i] - model2[i]) ** 2
    e = np.sqrt(e)
    e = round(e, 2)
    error2.append(e)

# Choose between the two models. The model with less error with be the selected.
if sum(error1) > sum(error2):
    print("Linear Regression")
else:
    print("Average Price")

random_price = sorted(random_price)
model1 = sorted(model1)
model2 = sorted(model2)

# Graph details
fig, ax = plt.subplots()
ax.plot(random_price, 'o-', label='Random Prices')
ax.plot(model1, '-', label='Prediction with the Mean')
ax.set_xlabel('Price')
ax.set_title('Random Prices vs Model 1')
ax.legend()
plt.show()

# Graph the data
fig, ax = plt.subplots()
ax.plot(random_price, 'o', label='Prices')
ax.plot(model2, '-', label='Prediction with Linear Regression')
ax.set_xlabel('Price')
ax.set_title('Random Prices vs Model2')
ax.legend()
plt.show()
