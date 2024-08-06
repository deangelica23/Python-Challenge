# PyPoll

#import

import os

import csv

#create the path

csvpath = os.path.join("Resources", "election_data.csv")


#variables

total_votes = 0
candidates_names = []
candidate_votes = {}
percentage_votes_won = []
list_of_names = []
candidates = []
results = []

#opening path and reading

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader)


# The total number of votes cast
    for row in csvreader:
        total_votes += 1
        candidates_names = row[2]

        if candidates_names not in list_of_names:
                list_of_names.append(candidates_names)

        if candidates_names in candidate_votes:
            candidate_votes[candidates_names] += 1
        else:
            candidate_votes[candidates_names] = 1

# start of print analysis
print("Election Results")
print("----------------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------------")

# list of candidates who received votes /print analysis
# percentage of votes each candidate won /print analysis 
# total number of votes each candidate won /print anaysis 

for candidate, votes in candidate_votes.items():
     percentage = (votes / total_votes) * 100
     result_str = f"{candidate}: {percentage:.3f}% ({votes})"
     results.append(result_str)
     print(result_str)

# The winner of the election based on popular vote
print("----------------------------------")
winner = max(candidate_votes, key=candidate_votes.get)
print(f"Winner: {winner}")
print("----------------------------------")


# export all the analysis results to a txt file

output_path = os.path.join('analysis', 'election_results.txt')
with open(output_path, 'w') as file: 
     file.write("Election Results\n")
     file.write("-------------------------\n")
     file.write(f"Total Votes: {total_votes}\n")
     file.write("-------------------------\n")
     for result in results: 
          file.write(result + '\n')
     file.write("-------------------------\n")
     file.write(f"Winner: {winner}\n")
     file.write("-------------------------\n")

