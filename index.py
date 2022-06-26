import numpy as np
import pandas as pd
from sklearn.decomposition import PCA


def PCA_DF(df, nComponents):
    pca = PCA(
        n_components=nComponents,
        random_state=11
    )
    pca = pca.fit_transform(df)
    return pca


X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
pca = PCA_DF(X, 1)
print(pca)
