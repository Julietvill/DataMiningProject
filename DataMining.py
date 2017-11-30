from sklearn.svm import LinearSVC
from sklearn.feature_selection import SelectFromModel
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import svm
from sklearn.feature_selection import VarianceThreshold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
from sklearn.naive_bayes import BernoulliNB
from sklearn.neural_network import MLPClassifier
from sklearn.svm import LinearSVC
import numpy as np
import sys

#put the data in the correct format in order to use scikit
def setData( temp, max_coln ):
    data = np.zeros(shape=(1842, int(max_coln + 1)))

    for x in temp:
        row = int(x[0]) - 1
        col = int(x[1])
        data[row,col] = x[2]

    return data

#put the data in the correct format in order to use scikit
def setTestingData(temp, max_column):
    data = np.zeros(shape=(952, int(max_column + 1)))

    for x in temp:
        row = int(x[0]) - 1
        col = int(x[1])
        data[row,col] = x[2]

    return data


def getDataSets():
    training_file = 'training.txt'
    training_labels_file = 'label_training.txt'
    testing_file = 'testing.txt'

    class_labels = np.genfromtxt(training_labels_file)
    temp_training_data = np.genfromtxt(training_file)
    training_set = setData(temp_training_data, temp_training_data.max())
    temp_test_data = np.genfromtxt(testing_file)
    test_data = setTestingData(temp_test_data, temp_test_data.max())

    return training_set, class_labels, test_data


def main():
    # get data sets in numpy array to run scikit algorithms on
    data_set, data_labels, test_data = getDataSets() 
    X_train, y_train, X_test, y_test = train_test_split(data_set, data_labels, test_size=0.2)

    # Reduce features based off feature variance. Line below removes features that are 0 in more than 80% of the features
    sel = VarianceThreshold(threshold=(.05))
    feature_reduced_data_set = sel.fit_transform(data_set)
    print(feature_reduced_data_set.shape)

    # train various classifiers
    neigh = KNeighborsClassifier(n_neighbors=50)
    k_neighbor_scores = cross_val_score(neigh, feature_reduced_data_set, data_labels, cv=5)
    ann = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
    ann_scores = cross_val_score(ann, feature_reduced_data_set, data_labels, cv=5)
    svm = LinearSVC()
    svm_scores = cross_val_score(svm, feature_reduced_data_set, data_labels, cv=5)

    # print accuracy Score of KNeighbor
    print("K_N Accuracy: %0.2f (+/- %0.2f)" % (k_neighbor_scores.mean(), k_neighbor_scores.std() * 2))
    print("ANN Accuracy: %0.2f (+/- %0.2f)" % (ann_scores.mean(), ann_scores.std() * 2))
    print("SVM Accuracy Score: %0.2f (+/- %0.2f)" % (svm_scores.mean(), svm_scores.std() * 2))
    

if __name__ == '__main__':
    main()