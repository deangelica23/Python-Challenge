# PyPoll
import os

import csv

csvpath = os.path.join("Resources", "election_data.csv")


# In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.
# You will be given a set of poll data called election_data.csv. 
# The dataset is composed of three columns: "Voter ID", "County", and "Candidate". 
# Your task is to create a Python script that analyzes the votes and calculates each of the following values:

total_votes = 0
candidates_names = []
candidate_votes = {}
percentage_votes_won = []
list_of_names = []


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    header = next(csvreader)


# The total number of votes cast
    for row in csvreader:
        total_votes += 1
        
        candidates_names = row[2]
        
        if candidates_names not in list_of_names:  #need this
                list_of_names.append(candidates_names)  #need this
        
        if candidates_names in candidate_votes:
            candidate_votes[candidates_names] += 1
        else:
            candidate_votes[candidates_names] = 1  
        
print(f"Total Votes: {total_votes}")


print(f"Candidates Names: {candidates_names}" )
for name in list_of_names:
    print(name)

#         #candidate = row[2]
#         if candidate in candidate_votes:
#             candidate_votes[candidate] += 1
#             else:
#                 candidate_votes[candidate] = 1

# print(candidate_votes)




# A complete list of candidates who received votes



# The percentage of votes each candidate won

# percentage_votes_won = {}
#     for candidate, votes in candidate_votes.items():
#         percentage = (votes / total_votes) * 100
#         percentage_votes_won[candidate] = round(percentage, 3)
# print(percentage_votes_won)





# The total number of votes each candidate won

# The winner of the election based on popular vote

# winner = max(candidate_votes, key=candidate_votes.get)
# print(f"Winner: {winner}")

# # In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# output_file = "election_results.txt"
# with open(output_file, 'w') as file:
#     file.write("Election Results\n")
#     file.write("-------------------------\n")
#     file.write(f"Total Votes: {total_votes}\n")
#     file.write("-------------------------\n")
#     for candidate, votes in candidate_votes.items():
#             file.write(f"{candidate}: {percentage_votes_won[candidate]}% ({votes})\n")
#     file.write("-------------------------\n")
#     file.write(f"Winner: {winner}\n")
#     file.write("-------------------------\n")

# print("Analysis results have been exported to 'election_results.txt'.")