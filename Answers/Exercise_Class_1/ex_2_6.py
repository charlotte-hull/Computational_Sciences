import numpy as np
import matplotlib.pyplot as plt

from Answers.Exercise_Class_1.ex_2_3 import f
from Answers.Exercise_Class_1.ex_2_4 import fibonacci


n=10
x=np.arange(n)

f_array=[f(n) for n in x]

fibonacci_array = [fibonacci.evaluate(n) for n in x]

print(fibonacci_array)

plt.plot(x,f_array,color='firebrick',marker='x',label='Evaluated using a for loop')
plt.plot(x,fibonacci_array,color='cornflowerblue',label='Evaluated using a class')
plt.xlabel('$n$')
plt.ylabel('$f_n$')
plt.legend()
plt.show()
