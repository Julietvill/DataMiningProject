from sklearn.svm import LinearSVC
from sklearn.feature_selection import SelectFromModel
from sklearn import svm
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

def main():
    training_file = sys.argv[1]
    classes_file = sys.argv[2]
    testing_file = sys.argv[3]

    #pull the data from the texts
    class_data = np.genfromtxt( classes_file )
    temp = np.genfromtxt(training_file)
    data_set = setData( temp, temp.max() )

    # preprocess data through L1 based feature selection
    lsvc = LinearSVC(C=0.01, penalty="l1", dual=False).fit(data_set, class_data)
    model = SelectFromModel(lsvc, prefit=True)
    data_set_new = model.transform(data_set)

    # preprocess testing data
    temp_test_data = np.genfromtxt(testing_file)
    test_data = setTestingData(temp_test_data, temp_test_data.max())
    test_data_new = model.transform(test_data)

    # create classifier
    clf = svm.LinearSVC()
    clf.fit(data_set_new, class_data)
    results = clf.predict(test_data_new)

    for classifier in results:
        print(classifier)


main()