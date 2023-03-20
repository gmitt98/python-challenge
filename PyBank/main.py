#This is the code for our solution

import pandas as pd
import os
from dateutil.parser import parse

# First I get the path to the project directory
project_dir = os.path.dirname(os.path.abspath(__file__))
# Then I create the file path relative to the project directory
file_path = os.path.join(project_dir, "Resources", "budget_data.csv")
# Now I read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# These date formats did not play nice with regex to read the month value, so I went and found another solution using a new library
# Here I am using the parser module to add a column to my dataframe that is just the month
# I'm applying a lambda function using this module to each value in the date column and writing result that to the month column
df['Month'] = df['Date']. apply(lambda x: parse(x).month)
#print(df)
monthCount = df['Month'].nunique()
print(monthCount)