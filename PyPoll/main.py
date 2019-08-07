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

    # Loop through for total votes casted
    for row in csvreader:

        totalVotesCasted = totalVotesCasted + 1

        # Add candidates to list
        if row[2] not in candidatesWithVotes.keys():
            candidatesWithVotes[row[2]] = 0

        candidatesWithVotes[row[2]] = candidatesWithVotes[row[2]] + 1

def printResults(resultsFile, result):
    print(result)
    resultsFile.write(result + "\n")

with open("Results.txt", "w") as resultsFile:
    printResults(resultsFile, "Election Results")
    printResults(resultsFile, "-" * 25)
    printResults(resultsFile, f"Total Votes: {totalVotesCasted:,}")
    printResults(resultsFile, "-" * 25)

    for candidate in candidatesWithVotes.keys():
        winPercentage = candidatesWithVotes[candidate] / totalVotesCasted
        printResults(resultsFile, f"{candidate}: {winPercentage:.3%} ({candidatesWithVotes[candidate]:,})")

    printResults(resultsFile, "-" * 25)
    printResults(resultsFile, "Winner: " + max(candidatesWithVotes, key=candidatesWithVotes.get))
    printResults(resultsFile, "-" * 25)