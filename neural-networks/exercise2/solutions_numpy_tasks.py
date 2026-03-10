import numpy as np
import matplotlib.pyplot as plt


# Task 1
def exercise_1(n, min_value, max_value):
    A = np.random.rand(n, n)  # create a matrix
    A = np.triu(A)  # make it upper triangular
    A = A + A.T - np.eye(n) * np.diag(A)  # mirror and fix diagonal
    return A * (max_value - min_value) + min_value  # scale and shift


a = exercise_1(50, 2, 4)
plt.hist(a.flatten())
plt.show()

# Task 2
a = np.random.rand(7, 3)


def normalisation(matrix):
    zero_mean = (matrix - np.mean(matrix, axis=1, keepdims=True))
    unit_variance = zero_mean / np.std(matrix, axis=1, keepdims=True)
    increasing_variance = unit_variance * np.atleast_2d(np.sqrt((np.arange(matrix.shape[0]) + 1))).T
    return increasing_variance


result = normalisation(a)
print("Resulting matrix:\n", result, "\n")
print("Mean: \n", np.mean(normalisation(a), axis=1), "\n")
print("Variance: \n", np.var(normalisation(a), axis=1), "\n")


# Task 3
def inverse(m1, m2):
    assert m1.shape[0] == m2.shape[1] & m2.shape[0] == m1.shape[1], "Incompatible matrices"
    # return np.all(m1 @ m2 == np.eye(m1.shape[0]))
    return np.allclose(m1 @ m2, np.eye(m1.shape[0]))


matrix_1 = np.eye(5)
matrix_2 = np.eye(5)
print(inverse(matrix_1, matrix_2))

matrix_1 = np.random.randn(5, 5)
matrix_2 = np.eye(5)
print(inverse(matrix_1, matrix_2))

matrix_1 = np.random.randn(5, 5)
matrix_2 = np.linalg.inv(matrix_1)
print(inverse(matrix_1, matrix_2))


# Task 4
r_max = 9
n = 1000
c_x, c_y = 9, 8

r = np.sqrt(np.random.rand(n)) * r_max
angle = np.random.rand(n) * 2 * np.pi
# https://stackoverflow.com/questions/5837572/generate-a-random-point-within-a-circle-uniformly

x = np.atleast_2d(np.cos(angle) * r + c_x)
y = np.atleast_2d(np.sin(angle) * r + c_y)

result = np.concatenate((x, y), axis=0)
print(result.shape)

plt.scatter(result[0, :], result[1, :])
plt.show()
