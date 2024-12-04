import matplotlib.pyplot as plt

food = ['Mushroom','Pineapple','Prawns','Sausage','Spinach']
values = [0.17, 0.3, 0.085, 0.19, 0.3]

# Create the horizontal bar chart
plt.barh(food, values, color='green')

# Add tittle and labels
plt.title('Bar Chart')
plt.xlabel('Proportion of Total')
plt.ylabel('Categories')

# Show the plot
plt.show()