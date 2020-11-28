import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import numpy as np

class DecisionTree:
    """ Decision tree using the ID3 algorithm. """
    clf: DecisionTreeClassifier

    def __init__(self, train_data, train_labels):
        """ Builds the decision tree. """
        self.clf = DecisionTreeClassifier()
        self.clf.fit(train_data, train_labels)

    def predict(self, predict_data):
        """ Uses the decision tree to predict the passengers survival. """
        return self.clf.predict(predict_data)

    def save_tree(self, feature_labels, target_labels):
        """ Saves an image of the decision tree. """
        fig = plt.figure(figsize=(100,80))
        tree.plot_tree(self.clf, feature_names=feature_labels, class_names=target_labels, filled=True)
        fig.savefig("decision_tree.jpeg")
        