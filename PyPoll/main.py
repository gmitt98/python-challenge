# This is the solution for our code
# I am re-using some of my code from the PyBank project, specifically reading the file and writing the output

import pandas as pd
import os

# First I get the path to the project directory
projectDir = os.path.dirname(os.path.abspath(__file__))
# Then I create the file path relative to the project directory
filePath = os.path.join(projectDir, "Resources", "election_data.csv")
# Now I read the CSV file into a DataFrame
df = pd.read_csv(filePath)

#print(df.head)

totalVotes = len(df)
#print(totalVotes)

uniqueValues = df.nunique()
#print(uniqueValues)

candidateList = df['Candidate'].unique()
#print(candidateList)

resultsDict = {}

for i in candidateList:
    #print(i)
    votes = len(df[df["Candidate"]==i])
    #print(votes)
    voteShare = votes/totalVotes
    #print(voteShare)
    resultsDict[i] = (votes, voteShare)

#print(resultsDict)

#maxVote = max(resultsDict.values())
#print(maxVote)
winner = max(resultsDict, key=resultsDict.get)


firstOutput = """Election Results
-------------------------
Total Votes: {}
-------------------------
""".format(totalVotes)
print(firstOutput)

secondOutput = ""
for i,j in resultsDict.items():
    percentResult= round(j[1]*100,3)
    s = str(i) + " " + str(percentResult) + "% " + "(" + str(j[0]) + ")"
    #print(s)
    #print("")
    secondOutput = secondOutput + s + "\n"
print(secondOutput)

thirdOutput = """-------------------------
Winner: {}
-------------------------""".format(winner)

print(thirdOutput)

# for some odd reason this was saving my output to desktop instead of to project directory, so i am confirming that we are in the correct directory now
os.chdir(projectDir)

myText = open('results.txt', 'w')
myText.write(firstOutput)
myText.write(secondOutput)
myText.write(thirdOutput)
myText.close()