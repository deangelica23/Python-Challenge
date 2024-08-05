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
candidates = []

print("Election Results")
print("----------------------------------")

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

# print(candidate_votes)       
print(f"Total Votes: {total_votes}")
print("----------------------------------")
# A complete list of candidates who received votes

#print(f"Candidates Names: {candidates_names}" )
# for name in list_of_names:
#     print(name)


# The percentage of votes each candidate won


# percentage_votes_won = {}

results = []
for candidate, votes in candidate_votes.items():
     percentage = (votes / total_votes) * 100
     result_str = f"{candidate}: {percentage:.3f}% ({votes})"
     results.append(result_str)
     print(result_str)
print("----------------------------------")
winner = max(candidate_votes, key=candidate_votes.get)
print(f"Winner: {winner}")
print("----------------------------------")
#         percentage_votes_won[candidate] = round(percentage, 3)
# print(percentage_votes_won)



# The total number of votes each candidate won

# The winner of the election based on popular vote

# winner = max(candidate_votes, key=candidate_votes.get)
# print(f"Winner: {winner}")

# # In addition, your final script should both print the analysis to the terminal and export a text file with the results.


output_path = os.path.join('analysis', 'election_results.txt')
with open(output_path, 'w') as file: 
     file.write("Election Results\n")
     file.write("-------------------------\n")
     file.write(f"Total Votes: {total_votes}\n")
     file.write("-------------------------\n")

     #
     for result in results: 
          file.write(result + '\n')
          #file.write(results + '\n')
     file.write("-------------------------\n")

     file.write(f"Winner: {winner}\n")
     file.write("-------------------------\n")

# # print("Analysis results have been exported to 'election_results.txt'.")