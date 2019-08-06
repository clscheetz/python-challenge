import os 
import csv

# Set path
csvpath = os.path.join("PyPoll", "election_data.csv")

# Open the CSV file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read header row
    next(csvreader)

    # Initialize veriables
    totalVotesCasted = 0
    candidatesWithVotes = {}
    percentPerCandidate = 0.0
    totalWinsPerCandidate = 0
    winnerOfElection = ""

    # Loop through for total votes casted
    for row in csvreader:

        totalVotesCasted = totalVotesCasted + 1

        # Add candidates to list
        if row[2] not in candidatesWithVotes.keys():
            candidatesWithVotes[row[2]] = 0









    print("Election Results")
    print("-" * 25)
    print(f"Total Votes: {totalVotesCasted:,}")
    print("-" * 25)

    for candidate in candidatesWithVotes:
        print(f"{candidate}: ")
