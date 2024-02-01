# Assuming your 2D array is a list of lists
array_2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Find the number of rows and columns
num_rows = len(array_2d)
num_cols = len(array_2d[0]) if num_rows > 0 else 0

print("Number of rows:", num_rows)
print("Number of columns:", num_cols)
