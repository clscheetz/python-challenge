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
    greatestIncrease = 0
    greatestDecrease = 0
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
            totalProfitChange = totalProfitChange + currentProfit - previousMonthProfit

        # Set currentProfit to previousMonthProfit for next iteration  
        previousMonthProfit = currentProfit

        totalMonths = totalMonths + 1

        # Calculate greatest increase

        # Calculate greatest decrease







    print("Financial Analysis")
    print("-" * 25)
    print("Total Months: " + str(totalMonths))
    print("Total: $" + str(netProfit))
    print("Average Change: ${:.2f}".format(totalProfitChange / (totalMonths - 1)))
    print("Greatest Increase in Profits: ")
    print("Greatest Increase in Profits: ")
