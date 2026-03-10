import numpy as np

if __name__ == '__main__':
    ex_no = 4

    if ex_no == 1:
        # 1) Create a 7x7 matrix that has 0 on diagonals and 7 elsewhere
        # Solution
        # m = 7 + np.zeros((7, 7)) - np.eye(7) * 7
        m = 7 * (np.ones((7, 7)) - np.eye(7))
        print(m)

    elif ex_no == 2:
        # 2) Let's have 7 vectors stacked in a matrix A.
        # Calculate the Euclidean length of these 7 vectors by calling numpy functions.
        A = np.random.randn(3, 7)
        A_l = np.linalg.norm(A, axis=0)
        # print(A)
        print(A_l)

    elif ex_no == 3:
        # 3.1) Generate a matrix R of random shape (number of rows and cols from 2 to 10) and fill it with random
        # numbers from normal distribution with mean 42 and standard deviation 9.
        # Solution
        r, c = np.random.randint(2, 11), np.random.randint(2, 11)
        R = np.random.randn(r, c) * 9 + 42
        print(R)

        # 3.2 Verify that in the matrix R, the mean and the standard deviation are close to the desired values.
        # Solution
        print(np.mean(R), np.std(R))

    elif ex_no == 4:
        # 4.1) Generate a matrix M of shape 5x5 of increasing numbers (1, 2, ..., 25).
        M = np.arange(25).reshape(5, 5) + 1

        # 4.2) Create a matrix N of shape 5x5, that contains randomly generated zeros or ones, where the probability of
        # the element N_ij being 1 is defined by the inverse of the value M_ij.
        N = np.zeros((5, 5))
        mask = np.random.rand(5, 5)
        N[mask < 1 / M] = 1

        # 4.3 Statistically verify that your code is correct
        sum_values = np.zeros((5, 5))
        threshold_value = 0.01
        n_trials = 1000000
        for i in range(n_trials):
            N = np.zeros((5, 5))
            mask = np.random.rand(5, 5)
            N[mask < 1 / M] = 1
            sum_values += N

        distance_from_expectation = np.sum(np.abs(sum_values/n_trials - 1/M))
        print(f"Distance from expectation: {distance_from_expectation:0.4f}")
        if distance_from_expectation < threshold_value:
            print("The matrix N is correctly generated!")


