'''
Exercise 1.2.5 - Write a python program that constructs an array that has length 
n and as its k-th entry the k-th term of the Fibonacci sequence by using a for 
loop over the elements of the array. Then print the n-th element of the array. 

'''
#%%
import numpy as np
#%%
n = 10
fibonacci = np.zeros((n + 1), dtype=int)

for k, element in enumerate(fibonacci):
    if k == 0:
        fibonacci[k] = 0
    elif k == 1:
        fibonacci[k] = 1
    else:
        fibonacci[k] = fibonacci[k - 1] + fibonacci[k - 2]

print("array:", fibonacci)
print("sum of elements:", np.sum(fibonacci))
print("norm:", np.linalg.norm(fibonacci))
print("reverse array:", np.flip(fibonacci))
# %%