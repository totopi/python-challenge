'''In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)

You will be given two sets of poll data (election_data_1.csv and election_data_2.csv). Each dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:

The total number of votes cast

A complete list of candidates who received votes

The percentage of votes each candidate won

The total number of votes each candidate won

The winner of the election based on popular vote.

As an example, your analysis should look similar to the one below:

Election Results
-------------------------
Total Votes: 620100
-------------------------
Rogers: 36.0% (223236)
Gomez: 54.0% (334854)
Brentwood: 4.0% (24804)
Higgins: 6.0% (37206)
-------------------------
Winner: Gomez
-------------------------
Your final script must be able to handle any such similarly-structured dataset in the future (i.e you have zero intentions of living in this hillbilly town -- so your script needs to work without massive re-writes). In addition, your final script should both print the analysis to the terminal and export a text file with the results.  voterid county candidate'''

import os
import csv

def ElectionResults(filename):

    # Let's start with some variables we want to be zeroed
    totalVotes = 0
    popularVote = 0
    candidateList = []
    voteList = []
    percentageList = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')

        for row in csvreader:
            # Total number of votes cast
            totalVotes = totalVotes + 1

            # Complete list of candidates who received votes
            if (row[2] not in candidateList) and (row[2] != 'Candidate'):
                candidateList.append(row[2])
                voteList.append(1)
                percentageList.append(0)
            
            # Total number of votes each candidate won
            elif (row[2] != 'Candidate'):
                voteList[candidateList.index(row[2])] = voteList[candidateList.index(row[2])] + 1
            
        # Percentage of votes each candidate won
        for x in range(len(candidateList)):
            percentageList[x] = (voteList[x] / totalVotes) * 100

            # Winner of the election based on popular vote
            if (voteList[x] > popularVote):
                popularVote = voteList[x]
        winner = candidateList[voteList.index(popularVote)]

        #OUTPUTS#
        outputs = []
        outputs.append("Election Results")
        outputs.append("-------------------------")
        outputs.append("Total Votes: " + str(totalVotes))
        outputs.append("-------------------------")
        for x in range(len(candidateList)):
            outputs.append(candidateList[x] + ": " + "%.1f" % percentageList[x] + "% (" + str(voteList[x]) + ")")
        outputs.append("-------------------------")
        outputs.append("Winner: " + winner)
        outputs.append("-------------------------")
        # And loop them out
        for x in outputs:
            print(x)
        
        # And now I just borrow the code I used before and....
    textfile = filename + ".txt"
    files = open(textfile, "w")
    for x in outputs:
        files.write(x + "\n")
    files.close()
    #Presto it's done!
ElectionResults('raw_data\\election_data_1.csv')
ElectionResults('raw_data\\election_data_2.csv')