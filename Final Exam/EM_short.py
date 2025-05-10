import numpy as np, matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture

np.random.seed(0)
X = np.vstack([np.random.normal(-2,1,(300,2)), np.random.normal(2,1,(300,2))])

gmm = GaussianMixture(n_components = 2).fit(X)
labels = gmm.predict(X)

plt.scatter(X[:,0], X[:,1], c=labels, cmap='viridis', s=30)
plt.scatter(*gmm.means_.T, c='red', marker='x', s=200)
plt.title("GMM Clustering (EM Algorithm)")
plt.show()
