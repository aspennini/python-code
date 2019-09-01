'''
	Name of script: append_directory.py
	Description: appends all files in a given directory 
		and saves appended file within the directory
	Inputs: directory - string filepath to a directory of csv
					files to be appended
			save - True or False indicating whether appended
					csv file should be saved
	Outputs: dataframe of all appended files
'''
import os
import sys
import pandas as pd


def main(directory, save):
	df = pd.Dataframe()
	for filename in os.listdir(directory):
		filepath = directory + filename
		data = pd.read_csv(filepath)
		df = df.append(data)
		
	if save == "True":
		df.to_csv('{}/compiled_files.csv'.format(directory), index=False)
	
	return(df)
		

if __name__ == "__main"__":
	directory = sys.argv[1]
	save = sys.argv[2]
	main(directory, save)
	

