import sys
import numpy as np
from medpy.filter.smoothing import anisotropic_diffusion
from hspectral import generators, detectors, utils
import matplotlib.pyplot as plt
sys.path.insert(0, '../..')
from skimage.morphology import disk
from skimage.filters.rank import median
from sklearn.preprocessing import normalize

def test_RX():
    X, y = generators.generate_anomaly(random_state=2, n_anomalies = 3,
                                       a_size = 8,
                                       noise_scale = .3, shape=(100,100,50))
    sigma, inv_sigma, result = detectors.RX(X)
    detection = detectors.anisomedian_decision(result)

    # Plot something
    fig, ax = plt.subplots(3,1, figsize=(3,8))
    ax[0].imshow(y, cmap='gray')
    ax[0].set_title('Ground truth')
    ax[1].imshow(X[:,:,30], cmap='gray')
    ax[1].set_title('Sample band')
    ax[2].set_title('RX output')


    ax[2].imshow(detection, cmap='gray')


    # remove the x and y ticks
    for a in ax:
        a.set_xticks([])
        a.set_yticks([])

    plt.savefig('bar.png')

    assert False
