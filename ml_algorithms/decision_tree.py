# https://colab.research.google.com/drive/1YNBFXqtIOD8VzHE_TbHytybBOSHrZJ7A?usp=sharing
# https://medium.com/@lope.ai/decision-trees-from-scratch-using-id3-python-coding-it-up-6b79e3458de4

import matplotlib.pyplot as plt
from sklearn import tree
import numpy as np, pandas as pd, math

class DecisionTree:
    """ Decision tree using the ID3 algorithm. """
    __tree: dict
    

    def __init__(self, train_data: pd.DataFrame, train_labels: pd.DataFrame):
        """ Builds the decision tree. """
        self.__entropy_attr(train_data, 1)

        self.__invoke_tree(train_data, train_labels)
        self.save_tree()


    def predict(self, predict_data):
        """ Uses the decision tree to predict the passengers survival. """
        return [1]


    def show_tree(self, feature_labels, target_labels, save=True):
        """ Shows an image of the decision tree. """
        fig = plt.figure(figsize=(100,80))
        tree.plot_tree(self.__tree, feature_names=feature_labels, class_names=target_labels, filled=True)
        
        if save:
            fig.savefig("decision_tree.jpeg")
        else:
            plt.show()


    def __invoke_tree(self, data, labels):
        """ Builds the decision tree. """
        best_node = self.__best_attr(data)

        label = labels[best_node]
        self.__tree = {label:{}}
        
        np.delete(labels, best_node)

        for value in np.unique(data[:, best_node]):
            self.__tree[label][value] = self.__invoke_tree(self.__split(data, best_node), labels[:]) 


    def __entropy(self, data: pd.DataFrame):
        """ Calculates the entropy of the data. """
        classes, counts = np.unique(data.to_numpy()[:, -1:], return_counts=True)

        # Calculate the entropy for each class.
        probs = counts / data.shape[0]
        probs = -probs * np.log2(probs)

        return probs.sum()


    def __entropy_attr(self, data: pd.DataFrame, i: int):
        target = data.keys()[-1]

        classes = np.unique(data.to_numpy[:, -1])
        column = data.iloc[:, i]

        entropy = 0

        for value in np.unique(data[:, i]):
            denom = len(data[i][data[i] == value])
            entropy_inner = 0
            for c in classes:
                numer = len(data[i][data[i] == value][data[target] == c])
                frac = numer / denom
                entropy_inner += -frac * math.log2(frac)


    def __best_attr(self, data):
        """ Returns the best node (node with highest information gain). """
        init_entropy = self.__entropy(data)
        max_ig = 0
        best_attr = -1
        
        for i in range(data.shape[1] - 1):
            attributes = np.unique(data[:,i])
            attr_entropy = 0

            for attr in attributes:
                new_data = self.__split(data, i)
                prob = new_data.shape[0] / data.shape[0]

                attr_entropy += prob * self.__entropy(new_data)
            
            ig = init_entropy - attr_entropy

            print(ig)

            if (ig > max_ig):
                max_ig = ig
                best_attr = i

        return best_attr


    def __split(self, data, i):
        """ Cut out the ith column from the dataset. """
        return np.delete(data, i, 1)
