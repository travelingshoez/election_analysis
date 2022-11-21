# Create a filename variable to a direct or indirect path to the file.
from distutils import text_file
import os
file_to_save = os.path.join("election_analysis.txt")
# Use the open() function with the "w" mode we will write data to the file.
outfile = open(file_to_save, "w")
# Write counties to the file.
outfile.write("Counties in the election\n------------------------\nArapahoe\nDenver\nJefferson")
# Add our dependencies 
import csv 
import os 
# Assign a varibale to load a file from a path. 
file_to_load = os.path.join("election_results.csv")
# Assign a variable to save the file to a path. 
file_to_save = os.path.join("election_analysis.txt")

# Open the election results and read the file
with open(file_to_load) as election_results: 
    file_reader = csv.reader(election_results)

    # Read and Print the header row. 
    headers = next(file_reader)
    print(headers)


