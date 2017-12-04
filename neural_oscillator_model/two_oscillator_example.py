#

from scipy.integrate import ode
import matplotlib.pyplot as plt

ITERATION = 2000
TIME_UPPER_LIMIT = 50.0
INITIAL_VALUES = [0.0, 1.0, 0.0, 1.0]
OSCILLATOR_WEIGHTS = [1.5, 1.5]

T = 1.0
tau = 4.0
w = 1.0
b = 2.5


class TwoNeuralOscillator(object):
    """
    Matsuoka's Neural Oscillator Mdodel.
    http://www.cs.cmu.edu/~hgeyer/Teaching/R16-899B/Assignments/Matsuoka87BiolCybern.pdf

    This class is one dimensional one.
    """

    def __init__(self,
                 initial_values=INITIAL_VALUES,
                 decay_time=T, suppression_time=tau,
                 input_weight=w, bonding=b,  # parameters related to differential equations
                 oscillator_weights=OSCILLATOR_WEIGHTS,  # parameter related to bonding oscillators each other
                 time_upper_limit=TIME_UPPER_LIMIT, iteration=ITERATION # parameters related to time steps
                 ):
        self._time_upper_limit = time_upper_limit
        self._iteration = iteration
        self._dt = self._time_upper_limit / self._iteration

        self._inverse_decay_time = 1.0 / decay_time
        self._inverse_suppression_time = 1.0 / suppression_time
        self._input_weight = input_weight / decay_time

        self._oscillator_weight = []
        for oscillator_weight in oscillator_weights:
            weight = oscillator_weight * self._inverse_decay_time
            self._oscillator_weight.append(weight)

        self._bonding = bonding / decay_time

        self.solver = ode(self._differential_equation)
        self.solver.set_integrator(name="dop853")
        self.solver.set_initial_value(initial_values)

        self.times = []
        self.main_results_1 = []
        self.adaptive_results_1 = []
        self.main_results_2 = []
        self.adaptive_results_2 = []

    def _external_input(self, t):
        return 1.0

    def _differential_equation(self, time, term):

        # TODO: Required matrix representaion if 3 or 4 oscillator model is to be codeds.
        external_input = self._external_input(time)

        main_oscillator = []
        adaptive_oscillator = []

        main_oscillator.append(term[0])
        main_oscillator.append(term[1])

        adaptive_oscillator.append(term[2])
        adaptive_oscillator.append(term[3])

        dot_main = []
        dot_adaptive = []

        temp_dot_main = -self._inverse_decay_time * main_oscillator[0] \
                        + self._input_weight * external_input \
                        - self._oscillator_weight[0] * max(main_oscillator[1], 0.0) \
                        - self._bonding * adaptive_oscillator[0]
        temp_dot_adaptive = -self._inverse_suppression_time * adaptive_oscillator[0] \
                            + self._inverse_suppression_time * max(main_oscillator[0], 0.0)

        dot_main.append(temp_dot_main)
        dot_adaptive.append(temp_dot_adaptive)

        temp_dot_main = -self._inverse_decay_time * main_oscillator[1] \
                        + self._input_weight * external_input \
                        - self._oscillator_weight[1] * max(main_oscillator[0], 0.0) \
                        - self._bonding * adaptive_oscillator[1]
        temp_dot_adaptive = -self._inverse_suppression_time * adaptive_oscillator[1] \
                            + self._inverse_suppression_time * max(main_oscillator[1], 0.0)

        dot_main.append(temp_dot_main)
        dot_adaptive.append(temp_dot_adaptive)

        return [dot_main[0], dot_main[1], dot_adaptive[0], dot_adaptive[1]]

    def next(self):
        if self.solver.t > self._time_upper_limit:
            return

        self.solver.integrate(self.solver.t + self._dt)

        self.times.append(self.solver.t)
        self.main_results_1.append(self.solver.y[0])
        self.adaptive_results_1.append(self.solver.y[1])
        self.main_results_2.append(self.solver.y[2])
        self.adaptive_results_2.append(self.solver.y[3])


if __name__ == '__main__':
    oscillator = TwoNeuralOscillator()

    t = 0.0
    main_oscillator = 0.0
    adaptive_oscillator = 0.0
    for i in range(ITERATION):
        oscillator.next()

    plt.figure(0)
    plt.title('Two Neural Oscillator')

    plt.plot(oscillator.times, oscillator.main_results_1)
    plt.plot(oscillator.times, oscillator.main_results_2)

    plt.draw()
    plt.show()
