'''
Exercise 1.2.6 - Write a python program that plots the graph of the Fibonacci sequence
on a grid of integers by using the functions implemented in exercise_1_2_3.py and 
exercise_1_2_4.py and compare all three implemented approaches in one figure.
'''
#%%
import matplotlib.pyplot as plt

from compsci.exercise_1_2_3 import fibonacci_naive, fibonacci
from compsci.exercise_1_2_4 import Fibonacci
# %%
fibonacci_class = Fibonacci()

n_values = list(range(10))
fibonacci_naive_values = [fibonacci_naive(n) for n in n_values]
fibonacci_values = [fibonacci(n) for n in n_values]
fibonacci_class_values = [fibonacci_class.evaluate(n) for n in n_values]

plt.plot(n_values, fibonacci_naive_values, label="Naive", marker="o")
plt.plot(n_values, fibonacci_values, label="Recursive", marker="x")
plt.plot(n_values, fibonacci_class_values, label="Class", marker="s")
plt.xlabel(r"$n$")
plt.ylabel(r"$F_n$")
plt.legend()
plt.show()
# %%
