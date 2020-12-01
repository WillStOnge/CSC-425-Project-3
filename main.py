import numpy as np, pandas as pd
from ml_algorithms import DecisionTree, Genetic, SVM

def main():
    # ----------------------------------------------------------- #
    #                       Decision Tree                         #
    # ----------------------------------------------------------- #

    # Train the tree.
    train_data = pd.read_csv("datasets/decision_tree/titanic_train.csv").fillna(0)
    tree = DecisionTree(train_data.iloc[:, :-1], train_data.iloc[:, -1])
    tree.save_tree(train_data.columns, ['No', 'Yes'])

    # Use the tree to predict.
    test_data = pd.read_csv("datasets/decision_tree/titanic_test.csv").fillna(0)
    test_labels = tree.predict(test_data.to_numpy())

    print("Decision tree test labels:", test_labels)

    """
    # Output the predicted values to a CSV.
    pd.DataFrame({'PassengerId': test_data['PassengerId'],
                    'Survived': test_labels}).to_csv("dt_submission.csv")

    # Output the tree to an image file.
    tree.save_tree(train_data.columns, ['No', 'Yes'])
    """

    # ----------------------------------------------------------- #
    #                            SVM                              #
    # ----------------------------------------------------------- #

    # Initialize SVM.
    svm = SVM(pd.read_csv("datasets/svm/mnist_subset.csv", sep=",", index_col=0))

    # Print results of kernel and grid search.
    print("SVM RBF Kernel:", svm.run_kernel())
    print("SVM Linear Kernel:", svm.run_kernel("linear"))
    print("SVM Sigmoid Kernel:", svm.run_kernel("sigmoid"))
    print("SVM Grid Weights:", svm.grid_search())

    # ----------------------------------------------------------- #
    #                          Genetic                            #
    # ----------------------------------------------------------- #

    start_codes = list()
    correct_code = """def sequentialSearch(alist, item):
    pos = 0
    found = False
    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos+1
    return found"""
    start_codes.append("""def sequentialSearch(alist, item):
    pos = 0
    found = False
    while pos < len(alist) and not found:
        if alist[pos] != item:
            found = True
        else:
            pos = pos*2
    return found""")
    start_codes.append("""def sequentialSearch(alist, item):
    pos = 0
    found = False
    while pos > len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos+1
    return found""")

    # Run genetic algorithm
    genetic = Genetic(start_codes, correct_code)
    if genetic.execute():
        print("Genetic: Correct code found")
    else:
        print("Genetic: Correct code was not found")


if __name__ == "__main__":
    main()
