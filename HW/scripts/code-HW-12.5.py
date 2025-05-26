import numpy as np
import matplotlib.pyplot as plt

n_list = [1, 2, 5, 50]
num_samples = 100_000

mu = 0.5
sigma = 1 / np.sqrt(12)

plt.figure(figsize=(12, 8))

for i, n in enumerate(n_list, 1):
    X = np.random.uniform(0, 1, size=(num_samples, n))
    S = X.sum(axis=1)
    Z_n = (S - n * mu) / (sigma * np.sqrt(n))
    
    plt.subplot(2, 2, i)
    plt.hist(Z_n, bins=50, density=True, alpha=0.7, color='skyblue', edgecolor='k')
    plt.title(f'n = {n}')
    plt.xlabel('$Z_n$')
    plt.ylabel('Density')

plt.tight_layout()
plt.show()
