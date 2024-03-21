import csv

# Path to the CSV file
csv_file = 'PyPoll/Resources/election_data.csv'

# setup variables
total_votes = 0
candidates_votes = {}
votes = 0


# open CSV
with open(csv_file, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    for row in csvreader:
        # obtain the candidates name from the row
        name = row[2]
        total_votes +=1
        #add the candidates vote count
        if name not in candidates_votes:
            candidates_votes[name] = 1
        else:
            candidates_votes[name] +=1
        
#calc voting percentage

percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidates_votes.items()}

#identify max vote winner
winner = max(candidates_votes, key =candidates_votes.get)


# Print the analysis results
print("Election Results")
print("------------------")
print(f"Total Votes: {total_votes}")
print('-------------------')
for name, votes in candidates_votes.items():
    print(f"{name}: {percentages[name]:.2f}% ({votes})")
print('-------------------------')
print(f"Winner: {winner}")
print('----------------------------')
#Export results into a text file
output_file = 'Pypoll.txt'
with open (output_file, 'w') as file:
    file.write("Election Results\n")
    file.write("------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write('-------------------\n')
    for name, votes in candidates_votes.items():
        file.write(f"{name}: {percentages[name]:.2f}% ({votes})\n")
    file.write('-------------------------\n')
    file.write(f"Winner: {winner}\n")
    file.write('----------------------------')