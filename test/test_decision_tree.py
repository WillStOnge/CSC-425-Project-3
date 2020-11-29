import numpy as np, pandas as pd, unittest
from ml_algorithms import DecisionTree

class TestDecisionTree(unittest.TestCase):
    def test(self):
        train_data = pd.read_csv("datasets/decision_tree/titanic_train.csv", header=0).fillna(0)
        tree = DecisionTree(train_data)

        #test_data = pd.read_csv("datasets/decision_tree/titanic_test.csv").fillna(0)
        #test_labels = tree.predict(test_data.to_numpy())
        