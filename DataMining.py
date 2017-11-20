import numpy as np
import sys

data_set = []
feature_list = {}

def download_files():
	training_file = sys.argv[1]
	testing_file = sys.argv[2]
	with open( training_file , "r") as file:
		data = file.readlines()
		for line in data:
			user_ID, feature_ID, value = line.split(" ")
			feature_data = {feature_ID.strip() : value.strip()}
			User_data = {user_ID.strip() : feature_data}
			data_set.insert( len(data_set), User_data)
			if len( feature_list ) == 0:
				feature_list.update( {feature_ID.strip() : 1})
			else:
				if feature_ID.strip() in feature_list.keys():
					feature_list[feature_ID.strip()] += 1
				else:
					feature_list.update( {feature_ID.strip() : 1})

	file.close()

def preprocessing():
	threshold = sum( feature_list.values() )
	threshold /= len(feature_list)
	for features,values in feature_list.items():
		if values < threshold:
			del feature_list[ features ]


def main():
	download_files()
	preprocessing()
	for keys,values in feature_list.items():
		print(keys, " : ", values )		

main()


'''
for keys,values in feature_list.items():
	print(keys, " : ", values )		
'''
#This is for testing the data set!
'''
for data in data_set:
	for x in data:
		print (x)
		for y in data[x]:
			print (y,':',data[x][y])
'''