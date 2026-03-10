#!/usr/bin/python3

# Neural Networks (2-AIN-132/15), FMFI UK BA
# (c) Tomas Kuzma, Juraj Holas, Peter Gergel, Endre Hamerlik, Štefan Pócoš, Iveta Bečková 2017-2026

from perceptron import *
from util import *


task = 2  # TODO select task

if task == 1:
    # Data preparation
    data = np.loadtxt('linsep.dat')  # 'linsep.dat' / 'and.dat' / 'or.dat' / 'xor.dat'
    inputs = data[:, :-1]
    targets = data[:, -1].astype(int)
    (count, dim) = inputs.shape

    # # Plot input data
    # plot_dots(inputs, targets)

    model = Perceptron(dim, use_activation=True)
    errors = model.train(inputs, targets, alpha=0.1, eps=20, live_plot=True)

    # # Plot decision border (use if live_plot was False)
    # plot_decision(model.weights, inputs, targets)

    # Plot error during training
    plot_errors(errors)

if task == 2:
    N = 5

    x = np.atleast_3d(np.tile(np.arange(0, N), N).reshape(N, N))/N
    y = np.atleast_3d(np.tile(np.arange(0, N), N).reshape(N, N).T)/N

    # Build cartesian product of sequence arrays
    grid = np.concatenate((x, y), axis=2)

    # generate random slopes (k1, k2) and shift (q)
    k1 = np.random.randn()
    k2 = np.random.randn()
    q = np.random.rand()

    # calculate z values
    z = k1 * grid[:, :, 0] + k2 * grid[:, :, 1] + q

    z += 0.2 * np.random.randn(N, N)

    model = Perceptron(2, use_activation=False)
    errors = model.train(grid.reshape(N*N, 2), z.flatten(), alpha=0.01, eps=2000, live_plot=False)

    k1_pred, k2_pred, q_pred = model.weights

    z_pred = k1_pred * grid[:, :, 0] + k2_pred * grid[:, :, 1] + q_pred

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(x, y, z)
    ax.plot_surface(grid[:, :, 0], grid[:, :, 1], z_pred, cmap='viridis')
    use_keypress(plt.gcf())   # Use ' ' or 'enter' to close figure; 'q' or 'escape' to quit program
    plt.show()
