from mvpa2.suite import SimpleSOMMapper

import numpy as np
from numpy.random import uniform
from numpy import pi
from math import cos, sin
from matplotlib import pyplot as plt

SAMPLE_NUMBER = 25
ITERATION = 1000
LEARNING_RATE = 0.05

vectors = []

for i in range(SAMPLE_NUMBER):
    radius = uniform()
    radian = uniform(0.0, 2.0*pi)

    x = radius*cos(radian)
    y = radius*sin(radian)

    vectors.append([x, y])

vectors = np.array(vectors)

if __name__ == '__main__':
    print(vectors)

    som = SimpleSOMMapper((30, 20), ITERATION, learning_rate=LEARNING_RATE)
    som.train(vectors)

    # plt.imshow(som.K, origin='lower')

    mapped = som(vectors)

    plt.figure()
    plt.title('Vector SOM')

    # SOM's kshape is (rows x columns), while matplotlib wants (X x Y)
    for i, m in enumerate(mapped):
        plt.quiver(m[1], m[0], vectors[i][0], vectors[i][1])

    plt.draw()
    plt.show()

