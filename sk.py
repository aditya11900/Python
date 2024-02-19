import numpy as np
import pandas as pd

from matplotlib import pyplot as plt
from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer()
print(cancer.feature_names)

data = np.c_[cancer.data, cancer.target]
columns = np.append(cancer.feature_names, ["target"])
df = pd.DataFrame(data, columns=columns)
print(df.head())
print(df.shape)

print(df['target'].value_counts())


x = [cancer['target_names'][0], cancer['target_names'][1]]

y = [df['target'].value_counts()[1], df['target'].value_counts()[0]]

plt.figure(figsize=(5, 5))
plt.bar(x, y, color=['red', 'green'])
plt.show()

plt.figure(figsize=(10, 10))
plt.scatter(df['mean radius'], df['mean texture'], color=df['target'].map({1: 'red', 0: 'green'}))
plt.xlabel("mean radius")
plt.ylabel("mean texture")
plt.show()




