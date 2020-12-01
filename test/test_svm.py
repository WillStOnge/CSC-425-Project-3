import unittest, pandas as pd
from ml_algorithms import SVM

class TestSVM(unittest.TestCase):
    def test(self):
        # This also runs all the kernels, so there is no need to call each kernel.
        svm = SVM(pd.read_csv("datasets/svm/mnist_subset.csv", sep=",", index_col=0)).grid_search()
