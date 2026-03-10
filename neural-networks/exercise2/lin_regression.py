#!/usr/bin/python3

# Neural Networks (2-AIN-132/15), FMFI UK BA
# (c) Tomas Kuzma, Juraj Holas, Peter Gergel, Endre Hamerlik, Štefan Pócoš, Iveta Bečková 2017-2026

import numpy as np
import matplotlib.pyplot as plt
from util import *

# # Generate data
# number of points
N = 100

# generate x values
x = np.arange(N)   # FIXME: vector [0, 1, 2, ..., N-1]

# generate random slope (k) and shift (q)
k = np.random.randn()   # FIXME: random number from normal distribution
q = np.random.rand()   # FIXME: random number from uniform distribution

# calculate y values
y = k * x + q   # FIXME: according to slides

# add noise
y += 5 * np.random.randn(N)  # FIXME: add vector of random values from normal distribution

# plot all points
plt.scatter(x, y)

# # Find k and q using linear regression
# first append ones to x
x = vector(x)   # FIXME: X should be matrix of two columns: first column is vector x, second column are ones
X = np.insert(x, 1, np.ones(N), axis=1)

# then find params
k_pred, q_pred =  np.linalg.inv(X.T @ X) @ X.T @ y # FIXME: according to slides

# predict ys and plot as a line
y_pred = k_pred * x + q_pred   # FIXME: according to slides

# plot predicted
plt.plot(x, y_pred, 'r')
use_keypress(plt.gcf())   # Use ' ' or 'enter' to close figure; 'q' or 'escape' to quit program
plt.show()
