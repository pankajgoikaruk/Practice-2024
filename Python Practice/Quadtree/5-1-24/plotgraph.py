import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Load crime data from csv file.
df = pd.read_csv('/workspaces/Practice-2024/Python Practice/Quadtree/5-1-24/data/DCR1.csv', encoding='latin-1')

df = df.head(1000)
print(df)

x = df['Longitude']
y = df['Latitude']

plt.scatter(x, y, s=1)  # Adjust the size based on your preference
plt.title('Crime Data Map')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()

#print(matplotlib.get_backend())