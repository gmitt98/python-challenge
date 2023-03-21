# This is the code for our solution
# I am moderately familiar with pandas dataframes

import pandas as pd
import os
from dateutil.parser import parse

# First I get the path to the project directory
projectDir = os.path.dirname(os.path.abspath(__file__))
# Then I create the file path relative to the project directory
filePath = os.path.join(projectDir, "Resources", "budget_data.csv")
# Now I read the CSV file into a DataFrame
df = pd.read_csv(filePath)

# From inspecting the dataframe earlier, we see that it contains one month entry per row, in chrolologically increasing order
# The total number of months is the total number of rows in the dataframe
totMonths = len(df)

# Get the sum of all profits and losses with the sum method
totalSum = df['Profit/Losses'].sum()

# Get the difference between rows with the diff method - this gives us a dataframe to run the next stats on
profitDiff = df['Profit/Losses'].diff()

# Get the average of the differences
avgChange = profitDiff.mean()

# Get the max and min changes by month, as well as the index (row number) where those occurs, so we can read the month where they occur
maxIncrease = profitDiff.max()
maxIncreaseIndex = profitDiff.idxmax()
minIncrease = profitDiff.min()
minIncreaseIndex = profitDiff.idxmin()

# Get the date that goes along with the min and max differences - by reading the data column at the index we just found above
maxIncreaseDate = df.loc[maxIncreaseIndex, 'Date']
minIncreaseDate = df.loc[minIncreaseIndex, 'Date']

# Create the output string we are going to print and save to text. This string needs to take the calculated variables from above
myOutput = """Financial Analysis
----------------------------
Total Months: {}
Total: ${}
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