#

from scipy.integrate import ode
import matplotlib.pyplot as plt

ITERATION = 1000
TIME_UPPER_LIMIT = 8.0
INITIAL_VALUES = [0.0, 0.0]

T = 1.2
w = 1.0
b = 2.5


class OneNeuralOscillator(object):
    """
    Matsuoka's Neural Oscillator Mdodel.
    http://www.cs.cmu.edu/~hgeyer/Teaching/R16-899B/Assignments/Matsuoka87BiolCybern.pdf

    This class is one dimensional one.
    """

    def __init__(self,
                 initial_values=INITIAL_VALUES,
                 decay_time=T, input_weight=w, bonding=b,  # parameters related to differential equations
                 time_upper_limit=TIME_UPPER_LIMIT, iteration=ITERATION # parameters related to time steps
                 ):
        self._time_upper_limit = time_upper_limit
        self._iteration = iteration
        self._dt = self._time_upper_limit/self._iteration

        self._inverse_decay_time = 1.0/decay_time
        self._weight = input_weight / decay_time
        self._bonding = bonding / decay_time

        self.solver = ode(self._differential_equation)
        self.solver.set_integrator(name="dop853")
        self.solver.set_initial_value(initial_values)

        self.times = []
        self.main_results = []
        self.adaptive_results = []

    def _external_input(self, t):
        return 1.0

    def _differential_equation(self, time, term):
        external_input = self._external_input(time)

        main_oscillator = term[0]
        adaptive_oscillator = term[1]

        dot_main = -self._inverse_decay_time * main_oscillator + self._weight * external_input \
                              - self._bonding * adaptive_oscillator
        dot_adaptive = -self._inverse_decay_time * adaptive_oscillator \
                       + self._inverse_decay_time * max(main_oscillator, 0.0)

        return [dot_main, dot_adaptive]

    def next(self):
        if self.solver.t > self._time_upper_limit:
            return

        self.solver.integrate(self.solver.t + self._dt)

        self.times.append(self.solver.t)
        self.main_results.append(self.solver.y[0])
        self.adaptive_results.append(self.solver.y[1])

if __name__ == '__main__':
    oscillator = OneNeuralOscillator()

    t = 0.0
    main_oscillator = 0.0
    adaptive_oscillator = 0.0
    for i in range(ITERATION):
        oscillator.next()

    plt.figure()
    plt.title('One Neural Oscillator')

    plt.plot(oscillator.times, oscillator.main_results)

    plt.draw()
    plt.show()
