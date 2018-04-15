from hspectral import utils
import numpy as np

class RX():
    def fit(self, X):
        shape = X.shape
        M = utils.convert2d(X)
        N, p = M.shape

        # Remove the data mean
        mean_signature = np.mean(M, axis = 0)
        M -= mean_signature

        # Compute covariance matrix
        sigma = np.matrix(np.cov(M.T))
        inv_sigma = np.array(sigma.I)

        # Calculate result
        result = np.zeros(N)
        for i in range(N):
            result[i] = np.abs((M[i,:][np.newaxis] @ inv_sigma @ M[i,:][np.newaxis].T)[0,0])

        result = np.reshape(result, (shape[0], shape[1]))

        return sigma, inv_sigma, result
