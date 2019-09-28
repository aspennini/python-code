'''
	Name of script: archive_directory.py
	Description: creates an archive directory and copies
					all csv files from a given directory 
					to the archive directory
	Inputs: output_dir - directory of files to archive
			archive_dir - directory to save archive folder
'''
import os
import sys
import shutil
from datetime import date

def main(output_dir, archive_dir):
    today = date.today().strftime("%Y_%m_%d")
    current_archive_dir = "{}/{}".format(archive_dir,today)
    if os.path.isdir == "True":
        pass
    else:
        os.mkdir("{}/{}".format(archive_dir,today))

    for filename in os.listdir(output_dir):
        if filename.endswith('.csv'):
            shutil.copy("{}/{}".format(output_dir,filename), current_archive_dir)
    return
    
if __name__ == "__main"__":
	directory = sys.argv[1]
	save = sys.argv[2]
	main(output_dir, archive_dir)