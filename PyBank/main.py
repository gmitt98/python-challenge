# This is the code for our solution

#import pandas as pd
import os
import csv

# First I get the path to the project directory
projectDir = os.path.dirname(os.path.abspath(__file__))
# Then I create the file path relative to the project directory
filePath = os.path.join(projectDir, "Resources", "budget_data.csv")

with open(filePath) as myFile:
    bankData=csv.reader(myFile)
    # Grab the headers
    headers = next(bankData)
    # Grab the first and second rows of data
    firstRow = next(bankData)
    secondRow = next(bankData)
    print(secondRow)
    # Initialize the values I'm going to use
    # I will need to track two rows at a time in order to calc averages so I run these manually on 2 rows then do a for loop
    totMonths = 2 # Since this first part processes the first two months, we initialize with this result
    totalSum = int(firstRow[1]) + int(secondRow[1]) # Total amount for the first two rows so far
    profitDiff = int(secondRow[1])-int(firstRow[1]) # This is the delta between the first two rows of data
    totalChange = profitDiff # After 2 rows of data, the average change is just the change in the first two rows
    maxIncrease = profitDiff # The average change on the first 2 rows is also the greatest change on 2 rows so far
    minIncrease = profitDiff # The average change on the first 2 rows is also the lowest change on 2 rows so far
    maxIncreaseDate = secondRow[0] # The date of the second month is the date of max change so far
    minIncreaseDate = secondRow[0] # The date of the second month is the date of min change so far
    previousMonthAmount = int(secondRow[1]) # This will be the previous month relative to the first row of the rest of the data set (which will start with row 3)
    # Begin looping through the remaining data
    for row in bankData:
        monthAmount = int(row[1])
        totMonths = totMonths+1 # Counting how many months we have processed so far
        totalSum = totalSum + monthAmount # Adding up the totals as we go
        profitDiff = monthAmount - previousMonthAmount # Calculating the change in profit between months
        totalChange = totalChange + profitDiff # Keeping a running sum of the change in profit between months
        if profitDiff > maxIncrease: # This if statement checks if we are seeing the highest profit change so far and records values if so
            maxIncrease = profitDiff
            maxIncreaseDate = row[0]
        if profitDiff < minIncrease: # This if statement checks if we are seeing the lowest profit change so far and records values if so
            minIncrease = profitDiff
            minIncreaseDate = row[0]
        previousMonthAmount=monthAmount # Setting the previous amount value in anticipation of jumping to the next row
    avgChange = totalChange / (totMonths-1) # The average change is the average of changes month to month, so the total changes is one less than the total of rows

# Create the output string we are going to print and save to text. This string needs to take the calculated variables from above
myOutput = """Financial Analysis
----------------------------
Total Months: {}
Total: ${:,.0f}
Average Change: ${:,.2f}
Greatest Increase in Profits: {} (${:,.0f})
Greatest Decrease in Profits: {} (${:,.0f})
""".format(totMonths,totalSum,avgChange,maxIncreaseDate,maxIncrease,minIncreaseDate,minIncrease)

# Print the results
print(myOutput)

# Create the file path to the analysis directory and changing directory to write our results there
outputDir = projectDir + '/Analysis'
os.chdir(outputDir)

# Write the outpout to the text file
myText = open('results.txt', 'w')
myText.write(myOutput)
myText.close()