'''
Exercise 1.2.4 - Write a Python program to generate the Fibonacci sequence up to
the n-th term using a class that
    1. for any current count k stores the respective k-1 th and k-2-th terms
        and the count as member variables,
    2. has an update member function that increases the count by 1 and stores
        the new k-1 th and k-2 th terms in the respective member variables,
    3. has an evaluate member function that updates until it reaches the given
        input value of n and returns the corresponding term.

Then print the n-th term.

What happens if you call the evaluate function multiple times with decreasing n? 
Is this intended behavior? What would you need to do in order to prevent 
logical errors? 
'''
#%%
class Fibonacci:
    k = 1
    F_kMinus1 = 1
    F_kMinus2 = 0

    def update(self):
        self.k += 1
        F_k = self.F_kMinus1 + self.F_kMinus2
        self.F_kMinus2 = self.F_kMinus1
        self.F_kMinus1 = F_k

    def evaluate(self, n):
        if n == 0:
            return self.F_kMinus2
        elif n == 1:
            return self.F_kMinus1
        else:
            while self.k < n:
                self.update()
        
        return self.F_kMinus1

    def reset(self):
        self.k = 1
        self.F_kMinus1 = 1
        self.F_kMinus2 = 0
# %%
if __name__ == "__main__":
    n = 10
    fibonacci = Fibonacci()
    print("evaluate for n = {}".format(n) + ":", fibonacci.evaluate(n))
    print("evaluate for n = {}".format(n - 1), "without reset:", fibonacci.evaluate(n - 1))
    fibonacci.reset()
    print("evaluate for n = {}".format(n - 1), "after reset:", fibonacci.evaluate(n - 1))
# %%
