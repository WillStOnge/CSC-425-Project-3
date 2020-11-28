import numpy as np, pandas as pd
from ml_algorithms import DecisionTree, Genetic

def main():
    # ----------------------------------------------------------- #
    #                       Decision Tree                         #
    # ----------------------------------------------------------- #
    """
    # Train the tree.
    train_data = pd.read_csv("datasets/decision_tree/titanic_train.csv").fillna(0)
    tree = DecisionTree(train_data.iloc[:, :-1], train_data.iloc[:, -1])
    tree.show_tree(train_data.columns, ['No', 'Yes'])

    # Use the tree to predict.
    test_data = pd.read_csv("datasets/decision_tree/titanic_test.csv").fillna(0)
    test_labels = tree.predict(test_data.to_numpy())
        
    # Output the predicted values to a CSV.
    pd.DataFrame({'PassengerId': test_data['PassengerId'],
                    'Survived': test_labels}).to_csv("dt_submission.csv")

    # Output the tree to an image file.
    tree.show_tree(train_data.columns, ['No', 'Yes'])
    """
    # ----------------------------------------------------------- #
    #                            SVM                              #
    # ----------------------------------------------------------- #



    # ----------------------------------------------------------- #
    #                          Genetic                            #
    # ----------------------------------------------------------- #

    correct_code = """def sequentialSearch(alist, item):
    pos = 0
    found = False
    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos+1
    return found"""
    start_code = """def sequentialSearch(alist, item):
    pos = 0
    found = False
    while pos < len(alist) and not found:
        if alist[pos] != item:
            found = True
        else:
            pos = pos*2
    return found"""

    genetic = Genetic(start_code, correct_code)
    if genetic.execute():
        print("Correct code found")
    else:
        print("Correct code was not found")


if __name__ == "__main__":
    main()
