import os
import csv


# Set path
csvpath = os.path.join("PyBank", "budget_data.csv")

# Open the CSV file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read header row
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Create variables for total months, net profit, average change, greatest increase, and greatest decrease
    totalMonths = 0
    netProfit = 0
    averageChange = 0
    greatestIncrease = {
        "date": "",
        "amount": 0
    }
    greatestDecrease = {
        "date": "",
        "amount": 0
    }
    totalProfitChange = 0
    previousMonthProfit = 0

    # Loop through looking for total months
    for row in csvreader:

        # Profit from current month
        currentProfit = int(row[1])

        # Calculate profit/loss
        netProfit = netProfit + currentProfit

        # Sum total change in profit/loss for each month after the 1st month 
        if totalMonths > 0:

            # Get current profit change
            currentProfitChange = currentProfit - previousMonthProfit

            totalProfitChange = totalProfitChange + currentProfitChange

            # Calculate greatest increase
            if currentProfitChange > greatestIncrease["amount"]:
                greatestIncrease["date"] = row[0]
                greatestIncrease["amount"] = currentProfitChange

            # Calculate greatest decrease
            if currentProfitChange < greatestDecrease["amount"]:
                greatestDecrease["date"] = row[0]
                greatestDecrease["amount"] = currentProfitChange

        # Set currentProfit to previousMonthProfit for next iteration  
        previousMonthProfit = currentProfit

        totalMonths = totalMonths + 1

def printResults(resultsFile, result):
    print(result)
    resultsFile.write(result + "\n")

with open("Results.txt", "w") as resultsFile:
    printResults(resultsFile, "Financial Analysis")
    printResults(resultsFile, "-" * 25)
    printResults(resultsFile, "Total Months: " + str(totalMonths))
    printResults(resultsFile, "Total: $" + str(netProfit))
    printResults(resultsFile, "Average Change: ${:.2f}".format(totalProfitChange / (totalMonths - 1)))
    printResults(resultsFile, "Greatest Increase in Profits: {} (${})".format(greatestIncrease["date"], greatestIncrease["amount"]))
    printResults(resultsFile, "Greatest Decrease in Profits: {} (${})".format(greatestDecrease["date"], greatestDecrease["amount"]))