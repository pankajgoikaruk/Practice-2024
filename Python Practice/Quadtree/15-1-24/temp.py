import pandas as pd

# Assuming you have a list of 50 points (replace this with your actual data)
points = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10),
          (11, 12), (13, 14), (15, 16), (17, 18), (19, 20),
          (21, 22), (23, 24), (25, 26), (27, 28), (29, 30),
          (31, 32), (33, 34), (35, 36), (37, 38), (39, 40),
          (41, 42), (43, 44), (45, 46), (47, 48), (49, 50)]

# Create an empty list to store DataFrames
dfs = []

# Loop through points and create a new DataFrame after every 5th point
for i in range(0, len(points), 5):
    subset_points = points[i:i+5]
    df = pd.DataFrame(subset_points, columns=['X', 'Y'])
    dfs.append(df)

# Display the resulting DataFrames
for i, df in enumerate(dfs, 1):
    print(f"DataFrame {i}:\n{df}\n")
