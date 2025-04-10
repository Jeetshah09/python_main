import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]  # x-axis values
y = [2, 3, 5, 7, 11]  # y-axis values

# Create a simple line plot
plt.plot(x, y, label="Line", color="blue", marker="o")

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Chart')

# Display the legend
plt.legend()

# Show the plot
plt.show()
