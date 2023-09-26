import pandas as pd

# Load the CSV file
data = pd.read_csv(r'C:\Users\tpw3615\OneDrive - Northwestern University\Desktop\python-challenge\PyPoll\Resources\election_data.csv')

# Task 1: Total number of votes cast
total_votes = len(data)

# Task 2: List of candidates who received votes
candidates = data['Candidate'].unique()

# Task 3 and 4: Calculate the percentage and total number of votes each candidate won
candidate_votes = data['Candidate'].value_counts()
candidate_percentages = (candidate_votes / total_votes) * 100

# Task 5: Find the winner
winner = candidate_votes.idxmax()

# Print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in candidates:
    print(f"{candidate}: {candidate_percentages[candidate]:.3f}% ({candidate_votes[candidate]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")
