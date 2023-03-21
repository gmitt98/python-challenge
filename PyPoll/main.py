# This is the solution for our code
# I a moderately familiar with pandas and dataframes

import pandas as pd
import os

# First I get the path to the project directory
projectDir = os.path.dirname(os.path.abspath(__file__))
# Then I create the file path relative to the project directory
filePath = os.path.join(projectDir, "Resources", "election_data.csv")
# Now I read the csv file into a dataframe
df = pd.read_csv(filePath)

# Total votes is the number of rows in the file (we could verify that there are no duplicates by comparing length to unique values, but we weren't asked to do that)
totalVotes = len(df)
# Get a lit of the candidates - this is the unique values in the candidate column
candidateList = df['Candidate'].unique()

# Put the election results in a dictionary. The key is the candidate, the values are their results
resultsDict = {}
for i in candidateList:
    votes = len(df[df["Candidate"]==i])
    voteShare = votes/totalVotes
    resultsDict[i] = (votes, voteShare)

# Find the key associated with the highest (aka 'max') result in the values
winner = max(resultsDict, key=resultsDict.get)

# I broke my output into three sections because I run a for loop in the second ond.
# First section outputs the total votes, with the formatting indicated in the assignment
firstOutput = """Election Results
-------------------------
Total Votes: {}
-------------------------
""".format(totalVotes)

# Second output section does a for loop on the candidates dictionary, and generates a string that has their result with the formatting requested
secondOutput = ""
for i,j in resultsDict.items():
    percentResult= round(j[1]*100,3)
    s = str(i) + " " + str(percentResult) + "% " + "(" + str(j[0]) + ")"
    secondOutput = secondOutput + s + "\n"

# Third section outpouts the winner
thirdOutput = """-------------------------
Winner: {}
-------------------------""".format(winner)

# Print the results
print(firstOutput)
print(secondOutput)
print(thirdOutput)

# Create the file path to the analysis directory and changing directory to write our results there
outputDir = projectDir + '/Analysis'
os.chdir(outputDir)

# Write the outputs to the text file, all outputs in a single file
myText = open('results.txt', 'w')
myText.write(firstOutput)
myText.write(secondOutput)
myText.write(thirdOutput)
myText.close()