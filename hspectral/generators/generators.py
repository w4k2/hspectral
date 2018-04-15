import numpy as np
import matplotlib.pyplot as plt

def generate_anomaly(shape = (100, 100, 50), n_anomalies = 2, a_size = 10,
                     random_state = None):
    np.random.seed(random_state)

    # Assigning shape of image
    X = np.zeros(shape)
    y = np.zeros(shape[:2])

    # Establishing position of anomalies
    positions_x = np.random.random_integers(shape[0] - a_size,
                                            size = n_anomalies)
    positions_y = np.random.random_integers(shape[1] - a_size,
                                            size = n_anomalies)

    # Drawing anomalies on ground_truth
    for i in range(n_anomalies):
        y[positions_x[i]:positions_x[i]+a_size,
          positions_y[i]:positions_y[i]+a_size] = 1

    print (positions_x)
    print (positions_y)``
    plt.imshow(y, cmap='gray')
    plt.savefig('foo.png')

    return X, y
