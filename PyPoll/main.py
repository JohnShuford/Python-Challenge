import os
import csv
import operator

#Setting the relative path
csv_path = os.path.join("Resources", "election_data.csv")

#Opening the CSV file
with open (csv_path, mode= "r", newline= "") as csv_file:
    #reading the file
    csv_reader = csv.reader(csv_file, delimiter = ',')

    #designating the header
    csv_header = next(csv_reader)

    #setting a dictionary and vote counter
    votes = 0
    top_vote = {"O_Tooley":0, "Correy":0, "Li": 0, "Khan": 0}

    #Counting the votes and adding the indiviual totals to the dictionary
    for row in csv_reader:
        votes += 1
        if row[2] == "Khan":
            top_vote["Khan"] += 1
        elif row[2] == "Correy":
            top_vote["Correy"] += 1
        elif row[2] == "Li":
            top_vote["Li"] += 1
        elif row[2] == "O'Tooley":
            top_vote["O_Tooley"] += 1

    #find the winner
    winner = max(top_vote.items(), key= operator.itemgetter(1))[0]
    
    line_1 = "Election Results"
    line_2 = "_ _ _ _ _ _ _ _ _ _ _"
    line_3 = f"Total Votes: {votes}"
    line_4 = "_ _ _ _ _ _ _ _ _ _ _"
    line_5 = f"Khan: {(round((((top_vote['Khan'])/(votes))*100),2))}% {top_vote['Khan']}"
    line_6 = f"Correy: {(round((((top_vote['Correy'])/(votes))*100),2))}% {'Correy'}"
    line_7 = f"Li: {(round((((top_vote['Li'])/(votes))*100),2))}% {top_vote['Li']}"
    line_8 = f"O'Tooley: {(round((((top_vote['O_Tooley'])/(votes))*100),2))}% {top_vote['O_Tooley']}"
    line_9 = "* * * * * * * * * * * * * *"
    line_10 = f"Winner: {winner}"
    line_11 = "* * * * * * * * * * * * * *"

print(line_1 + "\n" + line_2 + "\n" + line_3 + "\n" + line_4 + 
"\n" + line_5 + "\n" + line_6 + "\n" + line_7 + "\n" + line_8 + 
"\n" + line_9 + "\n" + line_10 + "\n" + line_11)

txt_path = os.path.join("Analysis", "final_vote.txt")
with open (txt_path, mode = "w") as text:
    text.writelines(line_1 + "\n" + line_2 + "\n" + line_3 + "\n" + line_4 + 
"\n" + line_5 + "\n" + line_6 + "\n" + line_7 + "\n" + line_8 + 
"\n" + line_9 + "\n" + line_10 + "\n" + line_11)
