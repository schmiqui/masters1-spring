# Neural Networks (2-AIN-132/15), FMFI UK BA
# (c) Tomas Kuzma, Juraj Holas, Peter Gergel, Endre Hamerlik, Štefan Pócoš, Iveta Bečková 2017-2026

from util import *


class Perceptron:
    def __init__(self, dim, use_activation):
        self.dim = dim
        self.weights = np.random.rand(dim + 1)  # VELKOST VSTUPU + (BIAS)   # FIXME: initialize the weight vector
        print(self.weights)
        print(self.weights.shape)
        self.use_activation = use_activation

    def train(self, inputs, targets, alpha=0.1, eps=20, live_plot=False):
        if live_plot:
            plot_decision(self.weights, inputs, targets, show=False)
            interactive_on()

        (count, _) = inputs.shape
        errors = []

        for ep in range(eps):
            print('Ep {:3d}/{}: '.format(ep+1, eps), end='')
            overall_error = 0  # Overall error for episode

            for idx in np.random.permutation(count):  # "for each idx in random order"
                x = add_bias(inputs[idx])   #PRE KAZDY TRENOVACI INPUT PRIDAJ BIAS                     # FIXME: retrieve the current input and add bias
                d = targets[idx]    # DOSTAN CHCENY VYSLEDOK                     # FIXME: retrieve the current target value

                net = self.weights.T @ x     # VSTUP DO PRECPETRONU - VSTUP * VAHA                 # FIXME: compute the "net" values

                if self.use_activation:
                    y = 1.0 if net >= 0 else 0.0                    # FIXME: set the output
                else:
                    y = net                      # FIXME: set the output

                e = d - y       # VYPOCITAJ ERROR - to je CHCENA HODNOTA - PREDIKOVANA               # FIXME: compute error on this input
                overall_error += e**2 / 2.0 # CELKOVY ERROR JE error plus 1/2 * ERRORˆ2 - INAK POVEDANE ERROR JE E = 1/2 * SUM[x] (vystup[x] - predikcia[x])ˆ2

                self.weights += alpha * e * x      # VAHY UPDATNES AKO W = W + ALFA * E * X       # FIXME: update the weights

            errors.append(overall_error)
            print('E = {:.3f}'.format(overall_error))

            if live_plot:
                clear()
                plot_decision(self.weights, inputs, targets, show=False)
                redraw()

        if live_plot:
            plt.show(block=True)
            interactive_off()

        return errors
