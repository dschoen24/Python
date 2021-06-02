import os
import csv

os.getcwd()

file_path = os.path.join(os.getcwd(), "Resources", "election_data.csv")
print(file_path)

# Variables
total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

#open csv file in read mode
with open(file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    #Skip the header row
    next(csvreader, None)
    #Loop through each row in file
    for row in csvreader:
        #Count unique voters & store in variable total votes
        total_votes +=1
        #Loop through candidate name & count the times they appear then store in list
        #Use these values for percent calculation in print statements
        if row[2] == "Khan":
            khan_votes +=1
        elif row[2] == "Correy":
            correy_votes +=1
        elif row[2] == "Li":
            li_votes +=1
        elif row[2] == "O'Tooley":
            otooley_votes +=1

#Find the winner - create an index
candidates = ["Khan", "Correy", "Li", "O'Tooley"]
votes = [khan_votes, correy_votes, li_votes, otooley_votes]

#Zip the lists together & return winner using max function
dict_candidates_and_votes = dict(zip(candidates, votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

#Print summary of the analysis
khan_percent = (khan_votes/total_votes) *100
correy_percent = (correy_votes/total_votes) *100
li_percent = (li_votes/total_votes) *100
otooley_percent = (otooley_votes/total_votes) *100

#Print summary
print("Election Results")
print('\n')
print("-------------------------")
print('\n')
print(f"Total Votes:  {total_votes}")
print('\n')
print("-------------------------")
print('\n')
print(f"Khan: {khan_percent:.3f}% ({khan_votes})")
print(f"Correy: {correy_percent:.3f}% ({correy_votes})")
print(f"Li: {li_percent:.3f}% ({li_votes})")
print(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
print('\n')
print("-------------------------")
print('\n')
print(f"Winner: {key}")
print('\n')
print("-------------------------")

#Output file
output_file = os.path.join(os.getcwd(), "Analysis", "election_data.txt")

with open(output_file, "w") as datafile:
    datafile.write("Election Results")
    datafile.write('\n')
    datafile.write("-------------------------")
    datafile.write('\n')
    datafile.write(f"Total Votes:  {total_votes}")
    datafile.write('\n')
    datafile.write("-------------------------")
    datafile.write('\n')
    datafile.write(f"Khan: {khan_percent:.3f}% ({khan_votes})")
    datafile.write('\n')
    datafile.write(f"Correy: {correy_percent:.3f}% ({correy_votes})")
    datafile.write('\n')
    datafile.write(f"Li: {li_percent:.3f}% ({li_votes})")
    datafile.write('\n')
    datafile.write(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
    datafile.write('\n')
    datafile.write(f"-------------------------")
    datafile.write('\n')
    datafile.write(f"Winner: {key}")
    datafile.write('\n')
    datafile.write("-------------------------")
    