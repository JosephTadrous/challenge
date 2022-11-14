'''
Author: Joseph Tadrous
Description: A python script to read csv files from command line and combine them into a single file with an added column for the file name
'''

import sys

class CSVCombiner:
    def combine(self):
        # Get all headers and add filename header for our new column
        with open(sys.argv[1]) as file:
            print(file.readline()[:-1] + ',filename')
        # Go through all csv files and print out the lines with the filename
        for i in range(1, len(sys.argv)):
            file_path = sys.argv[i]
            file_name = file_path.split('/')[-1] # Get the file name from the path
            with open(file_path) as file:
                for j, line in enumerate(file):
                    # Skip the header
                    if j == 0:
                        continue
                    if line[-1] != '\n': # Check if it's last line
                        print(line + ',' + file_name)
                    else:
                        print(line[:-1] + ',' + file_name)

if __name__ == "__main__":
    combiner = CSVCombiner()
    combiner.combine()
    
