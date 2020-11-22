# Pypoll Python Exercise
import os
import csv

# Space out terminal output
print("\n\n")

# File path
path = "C:/Users/jforr/Rice Program/Class Materials/rice-hou-data-pt-10-2020-u-c/Homework/03-Python/Bank_Data_Review/Instructions/PyPoll/Resources/election_data.csv"

# Open Path
with open(path) as csvfile: 
    csvreader = csv.reader(csvfile,delimiter = ",")

    # Determine headers
    header = next(csvreader)

    # Define Variables
    total_votes = 0
    candidates = []
    vote_cast = []

    # Total Votes
    for row in csvreader:
        total_votes = total_votes + 1 # total votes

        if row[2] not in candidates:
            candidates.append(row[2]) # unique candidates
        
        vote_cast.append(row[2]) # build another array for vote counting (couldn't figure out multiple for loops; .seek() didn't work to rest csvreader)


    # Define variables
    cand_1 = 0
    cand_2 = 0
    cand_3 = 0
    cand_4 = 0
 
    # Votes per unique candidate
    for i in range(1, len(vote_cast)):
        if vote_cast[i] == candidates[0]:
            cand_1 = cand_1 + 1
        elif vote_cast[i] == candidates[1]:
            cand_2 = cand_2 + 1
        elif vote_cast[i] == candidates[2]:
            cand_3 = cand_3 + 1
        elif vote_cast[i] == candidates[3]:
            cand_4 = cand_4 + 1


    # Calculate and format percentages
    per_1 = "{:.3%}".format(cand_1 / total_votes)
    per_2 = "{:.3%}".format(cand_2 / total_votes)
    per_3 = "{:.3%}".format(cand_3 / total_votes)
    per_4 = "{:.3%}".format(cand_4 / total_votes)
    
    # Determine winner
    if per_1 > per_2 or per_3 or per_4:
        winner = candidates[0]
    elif per_2 > per_1 or per_3 or per_4:
        winner = candidates[1]
    elif per_3 > per_2 or per_1 or per_4:
        winner = candidates[2]
    elif per_4 > per_2 or per_3 or per_1:
        winner = candidates[3]
    else:
        winner = "Tie"
    

# Text file output
with open('C:/Users/jforr/Rice Program/Class Materials/rice-hou-data-pt-10-2020-u-c/Homework/03-Python/Bank_Data_Review/Instructions/PyPoll/PyPoll.txt', 'w') as text_file:
    # Print statements
    text_file.write("Election Results\n")
    text_file.write("-----------------------\n")
    text_file.write(f'Total Votes: {total_votes}\n')
    text_file.write("-----------------------\n")
    text_file.write(f'{candidates[0]}: {per_1} ({cand_1})\n')
    text_file.write(f'{candidates[1]}: {per_2} ({cand_2})\n')
    text_file.write(f'{candidates[2]}: {per_3} ({cand_3})\n')
    text_file.write(f'{candidates[3]}: {per_4} ({cand_4})\n')
    text_file.write("-----------------------\n")
    text_file.write(f'Winner: {winner}\n')
    text_file.write("-----------------------\n")

