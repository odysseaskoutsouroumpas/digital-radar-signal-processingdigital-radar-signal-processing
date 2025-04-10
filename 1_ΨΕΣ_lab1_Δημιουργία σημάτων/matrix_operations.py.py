
import matplotlib
matplotlib.use('Agg')
import numpy as np

#1
t = 2
print(t)
#2
A = np.array([[1, 3], [5, 6]])
print(A)
#3
u = np.array([2, 4, 5])
print(u)
#4
u1 = np.array([4, 9, 9, 8])
print(u1)
#5
u2 = u1 + 3
print(u2)
#6
upol = u1 * t
print(upol)
#7
upol2 = u1 * u2
print(upol2)
#8
print(len(u1))
#9
print(A.shape)
#10
print(A[0, 1])
#11
print(A[0, 0:2])
#12
t = np.arange(0, 1.1, 0.1)
print(t)
#12.1
help(np.array)
#12.2
import matplotlib.pyplot as plt
plt.plot(t)
plt.savefig('output.png')
