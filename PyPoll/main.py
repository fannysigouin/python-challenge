#import os module
import os

#import csv module
import csv

csvpath = os.path.join('Resources', 'election_data.csv')
with open(csvpath) as csvfile:
    #use DictReader class to read csv file as a dictionary, with headers as the keys
    csvreader = csv.DictReader(csvfile)
    csv_header = next(csvreader)

    #defining variables to be used in 2 for loops below
    total_votes = 0
    candidates = []
    candidate_votes = {}
    winner_votes = 0
    winner_name = ""

    # loop through the election_data dictionary to get the total number of votes and to tally the votes each candidate received
    for row in csvreader:
        total_votes += 1
        # setting the candidate variable as the name corresponding to the Candidate key in the dictionary
        candidate = row["Candidate"]
        # check if this is the first time this candidate has received a vote
        if candidate not in candidates:
            # if the candidate hasn't already received a vote, add them to the candidates list
            candidates.append(candidate)
            # add 1 to their vote count as this is the first instance
            candidate_votes[candidate] = 1
        # if this candidate is already in the candidates list, increase their existing vote count by 1 in the candidate_votes dictionary
        candidate_votes[candidate] = candidate_votes[candidate] + 1


# open the analysis text file to write the results of the for loop above 
analysis_path = 'analysis.txt'
with open(analysis_path, 'a') as file:
    #print to the terminal
    print("Election Results") 
    print("------------------------")
    print(f"Total Votes: {total_votes}")
    print("------------------------")

    #write the same thing in the text file
    file.write("Election Results\n")
    file.write("------------------------\n")
    file.write(f"Total Votes: {total_votes}")
    file.write("\n")
    file.write("------------------------\n")

    # new for loop to loop through the candidate_votes dictionary to get the percentage of votes for each candidate and the candidate who won the popular vote
    for candidate in candidate_votes:
        # store the corresponding number of votes for that candidate in a variable
        votes = candidate_votes[candidate]
        # calculate the percentage of votes received by that candidate
        vote_percentage = round((votes / total_votes) * 100, 3)
        # if statement to check if the number of votes received by that candidate is greater than the winning candidates' votes (set to 0 at the start of the loop based on variables defined earlier)
        # if it is greater, update the value of votes, set the value of winner_votes to the number of votes and set that candidate as the winner 
        if votes > winner_votes:
            winner_votes = votes
            winner_name = candidate
        
        # within the for loop: print to the terminal each candidate's name, their percentage of votes and their total votes
        print(f"{candidate}: {vote_percentage}% ({votes})")

        # within the for loop: write the same thing in the text file
        file.write(f"{candidate}: {vote_percentage}% ({votes})")
        file.write("\n")
        
    # outside of the for loop: print the winner's name
    print("------------------------")
    print(f"Winner: {winner_name}")

    # outside of the for loop: write the winner's name in the text file
    file.write("------------------------")
    file.write("\n")
    file.write(f"Winner: {winner_name}") 