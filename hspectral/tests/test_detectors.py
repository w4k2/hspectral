import sys
from hspectral import generators, detectors, utils
import matplotlib.pyplot as plt
sys.path.insert(0, '../..')


def test_RX():
    X, y = generators.generate_anomaly(random_state=2, n_anomalies = 3,
                                       a_size = 8,
                                       noise_scale = .3, shape=(100,100,50))
    estimator = detectors.RX()
    sigma, inv_sigma, result = estimator.fit(X)

    """
    # Plot something
    fig, ax = plt.subplots(3,1, figsize=(3,8))
    ax[0].imshow(y, cmap='gray')
    ax[0].set_title('Ground truth')
    ax[1].imshow(X[:,:,30], cmap='gray')
    ax[1].set_title('Sample band')
    ax[2].imshow(result, cmap='gray')
    ax[2].set_title('RX output')
    # remove the x and y ticks
    for a in ax:
        a.set_xticks([])
        a.set_yticks([])

    plt.savefig('bar.png')
    """
