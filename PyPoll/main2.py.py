# Load the CSV file
data = []
with open(r'C:\Users\tpw3615\OneDrive - Northwestern University\Desktop\python-challenge\PyPoll\Resources\election_data.csv', 'r') as file:
    lines = file.readlines()
    header = lines[0].strip().split(',')
    candidate_index = header.index("Candidate") if "Candidate" in header else -1
    if candidate_index == -1:
        print("No 'Candidate' column found in the CSV file.")
        exit()

    for line in lines[1:]:
        values = line.strip().split(',')
        if len(values) <= candidate_index:
            print("Invalid data format in the CSV file.")
            exit()

        data.append({
            header[0]: int(values[0]),
            header[1]: values[1],
            "Candidate": values[candidate_index]
        })

# Task 1: Total number of votes cast
total_votes = len(data)

# Task 2: List of candidates who received votes
candidates = set(entry['Candidate'] for entry in data)

# Task 3 and 4: Calculate the percentage and total number of votes each candidate won
candidate_votes = {}
for entry in data:
    candidate = entry['Candidate']
    if candidate in candidate_votes:
        candidate_votes[candidate] += 1
    else:
        candidate_votes[candidate] = 1

candidate_percentages = {}
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    candidate_percentages[candidate] = percentage

# Task 5: Find the winner
winner = max(candidate_votes, key=candidate_votes.get)

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