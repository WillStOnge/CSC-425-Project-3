import matplotlib.pyplot as plt, numpy as np, pandas as pd, math, time
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn import svm

class SVM:
    __data: pd.DataFrame


    def __init__(self, data: pd.DataFrame):
        self.__data = data


    def run_kernel(self, kernel="rbf"):
        """ Runs with a specified kernel: rfb (default), linear, and sigmoid. """
        X_tr = self.__data.iloc[:, :]  # iloc ensures X_tr will be a dataframe
        y_tr = self.__data.index
        weights = list()

        for i in range(1, 10):
            X_train, X_test, y_train, y_test = train_test_split(
                X_tr, y_tr, train_size = i / 10, random_state=30, stratify=y_tr
            )

            X_train = np.where(X_train > 0, 1, X_train)
            X_test = np.where(X_test > 0, 1, X_test)

            clf = svm.SVC(kernel=kernel, gamma=0.001)
            clf = clf.fit(X_train, y_train)
            mean = clf.score(X_test, y_test)

            weights.append(mean)

        return weights


    def grid_search(self):
        """ Performs a grid search. """
        grid_search_svc_weights = list()

        X_tr = self.__data.iloc[:, :]  # iloc ensures X_tr will be a dataframe
        y_tr = self.__data.index

        for i in range(1, 10):
            X_train, X_test, y_train, y_test = train_test_split(
                X_tr, y_tr, train_size = i / 10, random_state=30, stratify=y_tr
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
