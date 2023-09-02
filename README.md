# python-challenge
Module 3 Python Challenge

This Python challenge includes two programs: PyBank and PyPoll.

PYBANK
This program can be run using Python3 and the file main.py found in the PyBank folder.

In this program, the os and csv modules are first imported. The os module allows the creation of file paths across operating systems so the program runs regardless of the machine used. The csv module allows the program to read the imported .csv file to manipulate the data it contains.

The purpose of the PyBank program is to analyze budget data in the budget_data.csv file and return the following information:
1. The total number of months in the dataset
2. The net total amount of profit/losses over the entire period
3. The changes in profit/losses over the entire period and the average of those changes
4. The greatest increase in profits over the entire period, including the date and amount
5. The greatest decrease in profits over the entire period, including the date and amount

This is achieved by using a for loop to go through each row of the dataset in the .csv file. This loop will tally up the total number of months in the total_months variable, calculate the net profit/losses over the period and store it in the net_profit_losses variable, and calculate the changes in profit/losses from month to month and store it in the revenue_change_from_previous variable.

An if statement is used when calculating the changes in profit/losses to exclude the first month of the dataset, as the change from the previous month would be 0.

The changes in profit/losses are stored in a list called revenue_change_from_previous_month, while the corresponding month is stored in a list called month_change_from_previous. These two lists are zipped together and converted to a new list called converted_change_from_previous. 

This new, converted list is then used in a second for loop to get the highest increase and highest decrease in profits as well as the corresponding month for the increase and decrease.

When this program is run, it will output the results to the terminal as well as to a text file called analysis.txt. The results are the following:

Financial Analysis 
--------------------------- 
Total Months: 86
Total: $22564198
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)

-------------------------------------------------------------------------------

PYPOLL
This program can be run using Python3 and the file main.py found in the PyPoll folder.

In this program, the os and csv modules are first imported. The os module allows the creation of file paths across operating systems so the program runs regardless of the machine used. The csv module allows the program to read the imported .csv file to manipulate the data it contains.

For this program, DictReader was used to read the .csv file as a dictionary. This allows for easier manipulation of the data in the .csv file to get the results.

The purpose of the PyPoll program is to analyze poll data in the election_data.csv file and return the following information:
1. The total number of votes cast
2. A complete list of candidates who received votes
3. The percentage of votes each candidate won
4. The total number of votes each candidate won
5. The winner of the election based on popular vote

This is achieved first by using a for loop to go through each row of the .csv file. First, the loop will tally up the total number of votes. Then, it sets the candidate as the value corresponding to the "Candidate" key in the dictionary.

In order to get a list of the candidates who received votes, an if statement is used to make sure candidate names are not duplicated. First, an empty list named candidates is created. The if statement will check if the candidate's name is not in the list. If it is not, it will add the candidate's name to the list and increase their vote count by 1. If the candidate's name is already in the list, it will only increase their vote count by 1 but will not add their name to the list. The candidate's name and their corresponding total votes are added to a dictionary called candidate_votes.

A second for loop is then used to loop through each candidate in the candidate_votes dictionary to get the percentage of votes they each won and to determine the winner of the election.
The loop first stores the candidate's votes in a variable named votes. It then calculates the percentage of votes they received and stores it in a variable called vote_percentage. Then, an if statement checks if the number of votes received by that candidate is greater than the winner's votes. The winner_votes variable is initially set to 0, so the if statement will be true for the first iteration of the loop. It will then store the number of votes received by that candidate in the winner_votes variable and the candidate's name in the winner_name variable. 
For the second iteration of the loop, the if statement will now check if the new candidate's votes are greater than the previous candidate's. If so, it will update winner_votes and winner_name. If not, the loop will iterate a third time to find the winner.

When this program is run, it will output the results to the terminal as well as to a text file called analysis.txt. The results are the following:

Election Results
------------------------
Total Votes: 369711
------------------------
Charles Casper Stockham: 23.049% (85214)
Diana DeGette: 73.813% (272893)
Raymon Anthony Doane: 3.139% (11607)
------------------------
Winner: Diana DeGette