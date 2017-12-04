from mvpa2.suite import SimpleSOMMapper

import numpy as np
from matplotlib import pyplot as plt

ITERATION = 1000
LEARNING_RATE = 0.05

colors = np.array(
         [[0., 0., 0.],
          [0., 0., 1.],
          [0., 0., 0.5],
          [0.125, 0.529, 1.0],
          [0.33, 0.4, 0.67],
          [0.6, 0.5, 1.0],
          [0., 1., 0.],
          [1., 0., 0.],
          [0., 1., 1.],
          [1., 0., 1.],
          [1., 1., 0.],
          [1., 1., 1.],
          [.33, .33, .33],
          [.5, .5, .5],
          [.66, .66, .66]])

# store the names of the colors for visualization later on
color_names = ['black',
               'blue',
               'darkblue',
               'skyblue',
               'greyblue',
               'lilac',
               'green',
               'red',
               'cyan',
               'violet',
               'yellow',
               'white',
               'darkgrey',
               'mediumgrey',
               'lightgrey']

if __name__ == '__main__':
    som = SimpleSOMMapper((20, 30), ITERATION, learning_rate=LEARNING_RATE)
    som.train(colors)

    plt.figure()
    plt.imshow(som.K, origin='lower')
    plt.title('Color SOM')

    mapped = som(colors)

    # SOM's kshape is (rows x columns), while matplotlib wants (X x Y)
    for i, m in enumerate(mapped):
        plt.text(m[1], m[0], color_names[i], ha='center', va='center',bbox=dict(facecolor='white', alpha=0.5, lw=0))

    plt.draw()
    plt.show()
