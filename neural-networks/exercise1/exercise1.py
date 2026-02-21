import numpy as np

### Task 1
def task1():
    W = np.ones(shape=(7,7))
    W *= 7
    np.fill_diagonal(W, 0)
    return W

def task1_her():
    m = 7 + (np.zeros(shape=(7,7)) - np.eye(7)) * 7;


### Task 2
# Let’s have 7 three-dimensional vectors stacked in a matrix A.
# Calculate the length of these vectors by calling numpy
# functions.
def task2():
    A = np.random.rand(7,3)
    print(A)
    return np.linalg.norm(A, axis=1)

def task2_her():
    A = np.random.rand(3, 7)
    A_l = np.linalg.norm(A, axis=0)
    # print(A)
    print(A_l)

### Task 3
# Generate a matrix R of random shape (number of rows and
# cols from 2 to 10) and fill it with random numbers from
# normal distribution with mean 42 and standard deviation 9.
def task3():
    rows = np.random.randint(2,10)
    cols = np.random.randint(2,10)

    R = np.random.normal(size=(rows,cols), loc=42, scale=9)
    print(R)
    return R

def task3_her():
    rows = np.random.randint(2,11)
    cols = np.random.randint(2,11)
    R = np.random.randn(rows, cols) * 9 + 42

    print(np.mean(R), np.std(R))
    print(R)


### Task 4
# 4.1 Generate a matrix M of shape 5 × 5 of increasing numbers (1, 2, ..., 25).
# 4.2 Create a matrix N of shape 5x5, that contains randomly
# generated zeros or ones, where the probability of the element
# Nij being 1 is defined by the inverse of the value Mij.
# 4.3 Statistically verify that your solution is correct.
def task4():
    M = np.arange(1, 26)
    M.resize((5,5))
    print(M)


# def task4_her():
#     # 4.1)
#     M = np.arange(25).reshape((5,5)) + 1
#
#     # 4.2)
#     N = np.zeros((5,5))
#     mask = np.random.rand(5,5)
#     N[mask < 1 / M ] = 1
#
#     # 4.3)
#     sum values


if __name__ == '__main__':
    # W = task1()
    # print(W)

    # lengths = task2()
    # print(lengths)

    # R = task3()

    task4()

    # task4_her()