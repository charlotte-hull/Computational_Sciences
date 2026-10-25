import numpy as np

n=10
a=np.zeros(n+1,dtype=int)
a[1]=1
for k in range(n-1):
    a[k+2]=a[k]+a[k+1]

sum_a=np.sum(a)
norm_a=np.linalg.norm(a)
reverse_a=a[::-1]
print('The array is ',format(a),', the sum of its elements is ',format(sum_a),', the norm is ',norm_a,', and the array reversed is ',reverse_a,sep="")