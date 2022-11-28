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

#Step 1: County's options 
county_options = []

# Declare the empty dictionary.
candidate_votes = {}

# Step 1: Empty dictionary 
county_votes = {}

# Winning Candidate and Winning Count Tracker
winning_canidate = ""
winning_county = 0 
winning_count = 0
winning_percentage = 0 

# Step 2: Largest turnout string and variable winning county 
Largest_County_Turnout = ""
Largest_County = 0 

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

        # Step 3: Print the county name from each row
        county_name = row[1]
        
        if candidate_name not in candidate_options:
        # Add the candidate name to the candidate list. 
            candidate_options.append(candidate_name)

         # 2. Begin tracking that candidate's vote count. 
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count. 
        candidate_votes[candidate_name] += 1
            
        # Step 4a: Statement logical operator check county name accuired in Step 3
        # is in the county list you created in Step 1.   
        if county_name not in county_options:
            # Step 4b: Add the county name to the county list. 
            county_options.append(county_name)
        
            # Step 4c: Begin tracking that county's vote count. 
            county_votes[county_name] = 0

        # Step 5: Add a vote to that county's count. 
        county_votes[county_name] += 1

with open(file_to_save, "w") as txt_file:    
    # After opening the file print the final vote count to the terminal. 
    election_analysis = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"\n-------------------------\n"
        f"County Votes:\n")
    print(election_analysis, end= "") 
    # After printing the final vote count to the terminal save the final vote count to the text file.
    txt_file.write(election_analysis) 

    # Step 6a: Repetion Statement Get the county from the county dictionary that was created in Step 1
    for county_name in county_votes:
        # Step 6b: A variable to hold the county's votes as retreived from the county votes dict.
        votes = county_votes[county_name]
        # Step 6c: Wrtie a script that calculates the county's votes as a percentage of the total votes. 
        vote_percentage = float(votes) / float(total_votes) * 100
        county_results = (f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Step 6d: Print each county voter count and percentage to the terminal.
        print(county_results)
        # Step 6e
        txt_file.write(county_results)
        # Step 6f: Decision statement determines the county with the largest vote count
        #then adds that county and its vote count to the variables created in step 2.
        # Determine winning vote count, winning percentage, and winning candidate.    
            
    # Step 7: Print statemnt that prints out the largest turnout
    Largest_County_Turnout = (
        f"\n-------------------\n"
        f"Largest County Turnout: Denver {Largest_County_Turnout}\n"
        f"\n-------------------\n")
    print(Largest_County_Turnout)
    txt_file.write(Largest_County_Turnout)
    # Print the winnning county's results to txt file.   
    
    # Step 6E: Complieted in deliverable 2
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes.get(candidate_name)
        # 3. Calculate the percentage of votes. 
        vote_percentage = float(votes) / float(total_votes) * 100
        # to do: print out each candidates name, vote count, and percentage of
        # votes to the terminal. 
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidates voter count and percentage to the terminal.
        print(candidate_results)
        # Save the candidate results to our text file. 
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and winning candidate. 
        if (votes > winning_county) and (vote_percentage > winning_percentage):
            winning_county = votes
            winning_candidate = candidate_name 
            winning_percentage = vote_percentage
    # Print the winning candidate's results to the terminal. 
    winning_candidate_summary = (
        f"----------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_county:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-----------------------------\n")
    print(winning_candidate_summary)
    # Save the final vote count to the text file.
    txt_file.write(winning_candidate_summary)
 

  




   







