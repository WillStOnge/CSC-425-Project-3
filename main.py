import numpy as np, pandas as pd
from ml_algorithms import DecisionTree

def main():
    # ----------------------------------------------------------- #
    #                       Decision Tree                         #
    # ----------------------------------------------------------- #

    # Train the tree.
    train_data = pd.read_csv("datasets/decision_tree/titanic_train.csv").fillna(0)
    tree = DecisionTree(train_data.to_numpy()[:, :-1], train_data.to_numpy()[:, -1])
    tree.save_tree(train_data.columns, ['No', 'Yes'])

    # Use the tree to predict.
    test_data = pd.read_csv("datasets/decision_tree/titanic_test.csv").fillna(0)
    test_labels = tree.predict(test_data.to_numpy())
    
    # Output the predicted values to a CSV.
    pd.DataFrame({'PassengerId': test_data['PassengerId'],
                    'Survived': test_labels}).to_csv("dt_submission.csv")

    # Output the tree to an image file.
    tree.save_tree(train_data.columns, ['No', 'Yes'])

    # ----------------------------------------------------------- #
    #                            SVM                              #
    # ----------------------------------------------------------- #



    # ----------------------------------------------------------- #
    #                          Genetic                            #
    # ----------------------------------------------------------- #



if __name__ == "__main__":
    main()
