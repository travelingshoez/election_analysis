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

# 1. Initialize a total vote counter. 
total_votes = 0 

# Candidate options and candidate votes 
candidate_options = []

# 1. Declare the empty dictionary.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_canidate = ""
winning_count = 0 
winning_percentage = 0 

# Open the election results and read the file.
with open(file_to_load) as election_results: 
  file_reader = csv.reader(election_results) 

  # Read the header row.
  headers = next(file_reader)

  # Print each row in CSV file. 
  for row in file_reader:
    # Add to the total vote count. 
    total_votes += 1 

    # Print the candidate name from each row. 
    candidate_name = row[2]

    if candidate_name not in candidate_options:
        # Add the candidate name to the candidate list. 
         candidate_options.append(candidate_name)

        # 2. Begin tracking that candidate's vote count. 
         candidate_votes[candidate_name] = 0

    # Add a vote to that candidate's count. 
    candidate_votes[candidate_name] += 1    

# Determine the percentage of votes for each candidate by looping through the counts. 
# 1. Iterate through the candidate list. 
for candidate_name in candidate_votes:
  # 2. Retrieve vote count of a candidate.
  votes = candidate_votes[candidate_name]
  # 3. Calculate the percentage of votes. 
  vote_percentage = float(votes) / float(total_votes) * 100
  # to do: print out each candidates name, vote count, and percentage of
  # votes to the terminal. 
  print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
  if (votes > winning_count) and (vote_percentage > winning_percentage):
    # if true then set winning_count = votes and winning_percentage = 
    # vote_percentage. 
    winning_counts = votes 
    winning_percentage = vote_percentage
    # And, set the winning_canidate equal to the candidates name. 
    winning_candidate = candidate_name
winning_candidate_summary = (
  f"----------------------------\n"
  f"Winner: {winning_candidate}\n"
  f"Winning Vote Count: {winning_count:,}\n"
  f"Winning Percentage: {winning_percentage:.1f}%\n"
  f"-----------------------------\n")
print(winning_candidate_summary)

  




   







