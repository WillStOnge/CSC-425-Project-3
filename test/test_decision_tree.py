import numpy as np, pandas as pd, unittest
from ml_algorithms import DecisionTree

class TestDecisionTree(unittest.TestCase):
    def test(self):
        train_data = pd.read_csv("datasets/decision_tree/titanic_train.csv").fillna(0)
        tree = DecisionTree(train_data.to_numpy()[:, :-1], train_data.to_numpy()[:, -1])

        test_data = pd.read_csv("datasets/decision_tree/titanic_test.csv").fillna(0)
        test_labels = tree.predict(test_data.to_numpy())
        