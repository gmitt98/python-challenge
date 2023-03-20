# This is the code for our solution
# I am moderately familiar with pandas dataframes

import pandas as pd
import os
from dateutil.parser import parse

# First I get the path to the project directory
project_dir = os.path.dirname(os.path.abspath(__file__))
# Then I create the file path relative to the project directory
file_path = os.path.join(project_dir, "Resources", "budget_data.csv")
# Now I read the CSV file into a DataFrame
df = pd.read_csv(file_path)

#print(df.__len__())

# These date formats did not play nice with regex to read the month value, so I went and found another solution using a new library
# Here I am using the parser module to add a column to my dataframe that is just the month
# I'm applying a lambda function using this module to each value in the date column and writing result that to the month column
df['Month'] = df['Date']. apply(lambda x: parse(x).month)
df['Year'] = df['Date'].apply(lambda x: parse(x).year)
print(df)
# Now I can read the number of unique months in the file
monthCount = df['Month'].nunique()
print(monthCount) #prints '12', yay
yearCount = df['Year'].nunique()
monthCountTotal = df['Date'].nunique()
print(monthCountTotal)
print(yearCount)
# Clean up these comments, but... inspecting this data we see that there are only 2023 dates here
# So there are only 12 months!

totalSum = df['Profit/Losses'].sum()
print(totalSum)

profitDiff = df['Profit/Losses'].diff()
print(profitDiff)
avgChange = profitDiff.mean()
print(avgChange)
maxIncrease = profitDiff.max()
maxIncreaseIndex = profitDiff.idxmax()
minIncrease = profitDiff.min()
minIncreaseIndex = profitDiff.idxmin()

# OK now I will need to find the index at which these occur and then read the date at that index
print(maxIncrease)
print(maxIncreaseIndex)
print(minIncrease)
print(minIncreaseIndex)

maxIncreaseDate = df.loc[maxIncreaseIndex, 'Date']
minIncreaseDate = df.loc[minIncreaseIndex, 'Date']
print(maxIncreaseDate)
print(minIncreaseDate)
# All of thise seems to work per the instructions