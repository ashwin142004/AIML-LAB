import numpy as np
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture

# Generate sample data
np.random.seed(0)
X1 = np.random.normal(-2, 1, (300, 2))
X2 = np.random.normal(2, 1, (300, 2))
X = np.vstack([X1, X2])

# Fit Gaussian Mixture Model (GMM)
gmm = GaussianMixture(n_components=2)
gmm.fit(X)

# Predict cluster labels
labels = gmm.predict(X)

# Plot the results
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', s=30)
plt.scatter(gmm.means_[:, 0], gmm.means_[:, 1], c='red', marker='x', s=200)
plt.title("GMM Clustering (EM Algorithm)")
plt.show()
