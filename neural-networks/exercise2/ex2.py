import numpy as np
import matplotlib.pyplot as plt

def task1(n, min_value, max_value):
    A = np.random.rand(n,n)
    A = np.triu(A)
    A = A + A.T - np.eye(n) * np.diag(A)
    return A * (max_value - min_value) + min_value


a = task1(5, -100, 100)
print(a)
plt.hist(a.flatten())
plt.show()


# TASK 2
