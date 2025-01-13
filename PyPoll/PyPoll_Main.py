"""
This script analyzes election data from a dataset called "election_data.csv". 
The dataset contains three columns: "Voter ID", "County", and "Candidate".
The script performs the following tasks:
1. Calculates the total number of votes cast in the election.
2. Creates a complete list of candidates who received votes.
3. Calculates the percentage of total votes each candidate won.
4. Computes the total number of votes each candidate received.
5. Determines the winner of the election based on the popular vote.

 The results are printed to the console and text file, summarizing the election results, including 
 the total votes, vote percentages, and the winning candidate.

"""
import csv
import os

#Import file from the directory and declare where the output stored 
file_to_load = os.path.join("Resources", "election_data.csv") # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt") # Output file path

total_votes = 0 #counts total votes 
candidates_vote_dict = {}   #A dictionary where the candidate names are the keys, and the number of votes each candidate received is the corresponding value
percentage_vote = 0.00  #Percentage of vote a candidate received 
highest_vote = 0.00 #The highest number vote
winner_candidate = str  #The winning candidate

#open the csv and read the file
with open(file_to_load) as election_data:
    csvreader = csv.reader(election_data)

    header = next(csvreader) #skip the header
    
    #loop through each rows 
    for row in csvreader:     
        total_votes +=1     #count number of votes
        """
        This if condition first checks if the candidate is already in the candidates_vote_dict dictionary. 
        If the candidate is already in the dictionary, it will add one additional vote to the associated candidate. 
        However, if the candidate is not in the dictionary, the code will execute the else statement and 
        create an entry with the candidate's name, assigning them one vote.

        """
        if row[2] in candidates_vote_dict:
            candidates_vote_dict[row[2]] += 1
        else: 
            candidates_vote_dict[row[2]] = 1

#open file_to_output and write the results to txt file            
with open(file_to_output, "w") as txt_file:
    print("Election Results\n\n" + "-"*25)   #print into terminal
    txt_file.write("Election Results\n\n" + "-"*25) #write to file
    
    print(f'\nTotal Votes: {total_votes}\n\n' + "-"*25 + "\n")      #print into terminal           
    txt_file.write(f'\n\nTotal Votes: {total_votes}\n\n' + "-"*25 + "\n\n")   #write to file
 
    #Loop through each item in the candidates_vote_dict dictionary while accessing both the key (candidate name) and value (number of votes) of each entry.
    for key, value in candidates_vote_dict.items():
        
        percentage_vote = (value / total_votes) * 100   #Calculate the vote percentage by dividing each candidate's votes by the total votes
        
        print(f'{key}: {round(percentage_vote,3)}% ({value})\n')    #print percentage vote into terminal
        txt_file.write(f'{key}: {round(percentage_vote,3)}% ({value})\n\n') #write percentage vote into file

        #Track the vote percentage to determine who received the highest vote and declare the winner.
        if percentage_vote > highest_vote:
            highest_vote = percentage_vote
            winner_candidate = key
            
    print("-"*25 + f'\n\nWinner: {winner_candidate}\n\n' + "-"*25 ) #Print winning candidate into terminal
    txt_file.write("-"*25 + f'\n\nWinner: {winner_candidate}\n\n' + "-"*25 ) #Write winning candiate into file
              