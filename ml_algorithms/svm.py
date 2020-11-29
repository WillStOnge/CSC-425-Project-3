import math
import time
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV


def run_kernel(kernel="rfb":str):
    df = pd.read_csv("./datasets/SVM/mnist_subset.csv", sep=",", index_col=0)

    X_tr = df.iloc[:, :]  # iloc ensures X_tr will be a dataframe
    y_tr = df.index
    weigts = list()

    for i in range(1, 10):
        X_train, X_test, y_train, y_test = train_test_split(
            X_tr, y_tr, train_size=i / 10, random_state=30, stratify=y_tr
        )

        X_train = np.where(X_train > 0, 1, X_train)
        X_test = np.where(X_test > 0, 1, X_test)

        clf = svm.SVC(kernel=kernel, gamma=0.001)
        clf = clf.fit(X_train, y_train)
        mean = clf.score(X_test, y_test)

        weigts.append(mean)

    return weigts

def grid_search():
    grid_search_svc_weights = list()

    for i in range(1, 10):
        X_train, X_test, y_train, y_test = train_test_split(
            X_tr, y_tr, train_size=i / 10, random_state=30, stratify=y_tr
        )
        clf = GridSearchCV(
            estimator=svm.SVC(gamma=0.001),
            param_grid={"C": [1, 10], "kernel": ("linear", "rbf")},
        )

        X_train = np.where(X_train > 0, 1, X_train)
        X_test = np.where(X_test > 0, 1, X_test)

        clf = clf.fit(X_train, y_train)
        mean = clf.score(X_test, y_test)

        grid_search_svc_weights.append(mean)
        
    return grid_search_svc_weights


if __name__ == "__main__":
    default_weights = run_kernel()
    linear_weights = run_kernel("linear")
    sigmoid_weights = run_kernel("sigmoid")
    grid_weights = grid_search()

