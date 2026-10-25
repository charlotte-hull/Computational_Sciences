'''
Exercise 1.2.3 - Write a Python program to generate the Fibonacci sequence
up to the n-th term using a function that takes n as a parameter and returns
the n-th term, then print the n-th term.
'''
#%%
# naive implementation
def fibonacci_naive(n):
    a = 0
    b = 1
    count = 1
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        while count < n:
            c = a + b
            a = b
            b = c
            count += 1
    return b
# %%
# alternative: recursive implementation
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
#%%
if __name__ == "__main__":
    n = 10
    print("naive:", fibonacci_naive(n))
    print("recursive:", fibonacci(n))
# %%