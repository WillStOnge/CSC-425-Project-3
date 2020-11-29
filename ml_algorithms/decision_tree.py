import matplotlib.pyplot as plt
from sklearn import tree
import numpy as np, pandas as pd, math

class DecisionTree:
    """ Decision tree using the ID3 algorithm. """
    __tree: dict
    __data: pd.DataFrame
    

    def __init__(self, train_data: pd.DataFrame):
        """ Builds the decision tree. """
        self.__data = train_data
        self.__tree = self.__invoke_tree()

        print(self.__tree)


    def __best_attr(self):
        """ Returns the best node (node with highest information gain). """
        info_gain = []

        for key in self.__data.keys()[:-1]:
            info_gain.append(self.__entropy() - self.__entropy_attr(key))
        return self.__data.keys()[:-1][np.argmax(info_gain)]


    def __invoke_tree(self):
        """ Builds the decision tree. """
        target = self.__data.keys()[-1]
        tree = {}
        attr = self.__best_attr()
        tree[attr] = {}
        attribute_values = np.unique(self.__data[attr])
        
        for value in attribute_values:
            subtable = self.__data[self.__data[attr] == value].reset_index(drop=True)
            target_values, counts = np.unique(subtable[target], return_counts=True)

            if len(counts) == 1:
                tree[attr][value] = target_values[0]  
            else: 
                tree[attr][value] = self.__invoke_tree(subtable)

        return tree


    def __entropy(self):
        """ Calculates the entropy of the data. """
        target = self.__data.keys()[-1]
        values = self.__data[target].unique()
        entropy = 0

        for value in values:
            fraction = self.__data[target].value_counts()[value] / len(self.__data[target])
            if fraction >= 0:
                entropy += -fraction * np.log2(fraction)
        return entropy


    def __entropy_attr(self, attr):
        target = self.__data.keys()[-1]   
        target_variables = self.__data[target].unique()
        variables = self.__data[attr].unique()    
        final_entropy = 0

        for variable in variables:
            entropy = 0
            for target_variable in target_variables:
                num = len(self.__data[attr][self.__data[attr] == variable][self.__data[target] == target_variable])
                den = len(self.__data[attr][self.__data[attr] == variable])
                fraction = num / den

                if fraction >= 0:
                    entropy += -fraction * np.log2(fraction)
            final_entropy += -(den / len(self.__data)) * entropy

        return abs(final_entropy)
