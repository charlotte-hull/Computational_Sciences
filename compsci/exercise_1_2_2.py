'''
Exercise 1.2.2 - Write a Python program to generate the Fibonacci sequence
up to the n-th term using a while loop and print the n-th term.
'''
#%%
n = 10  # You can change this value to generate more terms
a = 0
b = 1
count = 1
if n == 0:
    print(a)
elif n == 1:
    print(b)
else:
    while count < n:
        c = a + b
        a = b
        b = c
        count += 1
    print(b)
# %%