import numpy as np

# Create a simple NumPy array
arr = np.array([10, 20, 30, 40, 50])

# Indexing: Accessing the first and last element
first_element = arr[0]
last_element = arr[-1]

# Slicing: Extracting elements from index 1 to 3 (exclusive)
slice = arr[1:4]

# Print the results
print("First element:", first_element)
print("Last element:", last_element)
print("Sliced array from index 1 to 3:", slice)
