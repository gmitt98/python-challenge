# This is the solution for our code

import os
import csv

# First I get the path to the project directory
projectDir = os.path.dirname(os.path.abspath(__file__))
# Then I create the file path relative to the project directory
filePath = os.path.join(projectDir, "Resources", "election_data.csv")

resultsDict = {}
totalVotes = 0
with open(filePath) as myFile:
    electionData=csv.reader(myFile)
    next(electionData) # Jumping past the headers
    for row in electionData:
        totalVotes = totalVotes + 1 # Count the ballot in the total
        cName = row[2] # Grab the candidate name for that ballot
        if cName not in resultsDict: # See if the candidate is in the results dictionary as a key, if not then create it with zero votes
            resultsDict[cName] = {"votes": 0, "voteShare": 0}
        resultsDict[cName]["votes"] = resultsDict[cName]["votes"] + 1 # Count the ballot for the candidate in the results dictionary
# Add the percentage vote share to the results dictionary
for i in resultsDict:
    resultsDict[i]["voteShare"] = resultsDict[i]["votes"]/totalVotes
# Now we have the results in a dictionary that goes {'candidate name': #-ballots, ... etc}

# Find the key associated with the highest result in the values by looping through the dictionary
# Using the same technique as I used in PyBank to hold on to the highest value found
winner = ""
winnerVotes = 0
for i in resultsDict:
    if resultsDict[i]["votes"] > winnerVotes:
        winnerVotes = resultsDict[i]["votes"]
        winner = i

# I broke my output into three sections because I run a for loop in the second one.
# First section outputs the total votes, with the formatting indicated in the assignment
firstOutput = """Election Results
-------------------------
Total Votes: {}
-------------------------
""".format(totalVotes)

# Second output section does a for loop on the results dictionary, and generates a string that has their result with the formatting requested
secondOutput = ""
for i in resultsDict:
    percentResult= round(resultsDict[i]["voteShare"]*100,3)
    s = str(i) + " " + str(percentResult) + "% " + "(" + str(resultsDict[i]["votes"]) + ")"
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