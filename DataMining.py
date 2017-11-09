#reading in the files, first we need to know how to
#read a file from the command line.
import sys
training_file = sys.argv[1]
testing_file = sys.argv[2]
output_file = sys.argv[3]

data_set = []
user_index = 1
feature_list = []

#read the data into the data structure
with open( training_file , "r") as file:
	data = file.readlines()
	for line in data:
		user_ID, feature_ID, value = line.split(" ")
		feature_data = {feature_ID.strip() : value.strip()}
		User_data = {user_ID.strip() :
						 {feature_ID.strip() : value.strip()} }
		data_set.insert(0, User_data)
file.close()