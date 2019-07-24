import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#This next line makes our charts show up in the notebook


table = pd.read_csv("./vic_housing_data.csv")
table.head()

plt.bar(x=np.arange(1,6),height=table['price'])

plt.title("Victoria Average Rental Price")
plt.xlabel("Bedrooms")
plt.ylabel("Price")
plt.show()