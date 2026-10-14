'''
Exercise 1.2 - Run the first basic program
'''
#%%
import matplotlib.pyplot as plt
#%%
# create grid and data points 
grid = []
data = []

# fill both with values 
for i in range(10):
    grid.append(i)
    data.append(i**2)

# plot the data on the grid
plt.plot(grid, data)
plt.xlabel('Grid')
plt.ylabel('Data')
plt.title('For loop example')
plt.show()
#%%
# create grid and data points using list comprehensions
grid = [i for i in range(10)]
data = [i**2 for i in grid]

plt.plot(grid, data)
plt.xlabel('Grid')
plt.ylabel('Data')
plt.title('List comprehension example')
plt.show()
# %%