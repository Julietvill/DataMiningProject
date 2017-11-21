import numpy as np
import sys

def setData( temp, max_coln ):
	data = np.zeros(shape=(1843, int(max_coln + 1)))

	for x in temp:
		row = int(x[0])
		col = int(x[1])
		data[row,col] = x[2]
	return data

def main():
	training_file = sys.argv[1]
	classes_file = sys.argv[2]
	testing_file = sys.argv[3]

	class_data = np.genfromtxt( classes_file )
	temp = np.genfromtxt(training_file)
	data_set = setData( temp, temp.max() )
	print(data_set)


main()