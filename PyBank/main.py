'''In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will be given two sets of revenue data (budget_data_1.csv and budget_data_2.csv). Each dataset is composed of two columns: Date and Revenue. (Thankfully, your company has rather lax standards for accounting so the records are simple.)

Your task is to create a Python script that analyzes the records to calculate each of the following:

The total number of months included in the dataset

The total amount of revenue gained over the entire period

The average change in revenue between months over the entire period

The greatest increase in revenue (date and amount) over the entire period

The greatest decrease in revenue (date and amount) over the entire period '''

import csv

def FinancialAnalysis(filename):
    #Different things that needed to be zeroed before stuff happens
    numberOfMonths = 0
    totalRevenue = 0
    revenueChangeTotal = 0
    revenueChangeLast = 0
    revenueChangeNow = 0
    greatestIncrease = ["",0]
    greatestDecrease = ["",0]
    thisLine = ""

    # In this with, the filename is called from the function argument so just do function(path) yay.
    with open(filename, newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')

        # I'm sure I made this much more complicated than it needs to be
        for row in csvreader:
            # for finding revenue changes, we'll call the previous iteration's current line var 
            lastLine = thisLine #before using it again as our current line this iteration 
            revenueChangeLast = revenueChangeNow # Same with the revenue change, for greatest etc

            # Time for stuff to happen, first make this line be the current line of the file
            thisLine = row

            # If we're in the header row, ignore it (if I left it blank it yelled at me so I did some tiny operation)
            if row[0] == "Date":
                x = 1
            
            # Don't do a certain thing if the last line was the header because str / int errors 
            elif lastLine[0] == "Date":
                totalRevenue = totalRevenue + int(thisLine[1])
                numberOfMonths = numberOfMonths + 1

            # Always be...
            else:
                # Adding up the total revenue
                totalRevenue = totalRevenue + int(thisLine[1])
                # Adding up the number of months
                numberOfMonths = numberOfMonths + 1
                # How has the revenue changed since the last row?
                revenueChangeNow = int(thisLine[1]) - int(lastLine[1])
                # We need the total change to calculate the average later
                revenueChangeTotal = revenueChangeTotal + revenueChangeNow
            # Check to see if our current change is more or less than the greatest increase/decrease   
            if (revenueChangeNow > greatestIncrease[1]):
                greatestIncrease = [row[0],revenueChangeNow]
            if (revenueChangeNow < greatestDecrease[1]):
                greatestDecrease = [row[0],revenueChangeNow]

    #OUTPUT#
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months:", numberOfMonths)
    print("Total Revenue: $"+ str(totalRevenue))
    print("Average Revenue Change: $" + str(revenueChangeTotal / numberOfMonths))
    print("Greatest Increase in Revenue: " + greatestIncrease[0] + " ($" + str(greatestIncrease[1]) + ")")
    print("Greatest Decrease in Revenue: " + greatestDecrease[0] + " ($" + str(greatestDecrease[1]) + ")")

# Now let's use that function on our two datasets.
FinancialAnalysis('raw_data\\budget_data_1.csv')
FinancialAnalysis('raw_data\\budget_data_2.csv')