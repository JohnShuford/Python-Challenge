import os
import csv
import operator

#Setting the relative path
csv_path = os.path.join("election_data.csv")

#Opening the CSV file
with open (csv_path, mode= "r", newline= "") as csv_file:
    #reading the file
    csv_reader = csv.reader(csv_file, delimiter = ',')

    #designating the header
    csv_header = next(csv_reader)

    #setting a dictionary and vote counter
    votes = 0
    top_vote = {"O'Tooley":0, "Correy":0, "Li": 0, "Khan": 0}

    for row in csv_reader:
        votes += 1
        if row[2] == "Khan":
            top_vote["Khan"] += 1
        elif row[2] == "Correy":
            top_vote["Correy"] += 1
        elif row[2] == "Li":
            top_vote["Li"] += 1
        elif row[2] == "O'Tooley":
            top_vote["O'Tooley"] += 1

    #find the winner
    winner = max(top_vote.items(), key= operator.itemgetter(1))[0]
    
    #values for the final results
    k_v = top_vote["Khan"]
    c_v = top_vote["Correy"]
    l_v = top_vote["Li"]
    o_v = top_vote["O'Tooley"]

    line_1 = "Election Results"
    line_2 = "_ _ _ _ _ _ _ _ _ _ _"
    line_3 = f"Total Votes: {votes}"
    line_4 = "_ _ _ _ _ _ _ _ _ _ _"
    line_5 = f"Khan: {(round((((k_v)/(votes))*100),2))}% {k_v}"
    line_6 = f"Correy: {(round((((c_v)/(votes))*100),2))}% {c_v}"
    line_7 = f"Li: {(round((((l_v)/(votes))*100),2))}% {l_v}"
    line_8 = f"O'Tooley: {(round((((o_v)/(votes))*100),2))}% {o_v}"
    line_9 = "* * * * * * * * * * * * * *"
    line_10 = f"Winner: {winner}"
    line_11 = "* * * * * * * * * * * * * *"

    print(line_1 + "\n" + line_2 + "\n" + line_3 + "\n" + line_4 + "\n" 
    + line_5 + "\n" + line_6 + "\n" + line_7 + "\n" + line_8 + "\n" + 
    line_9 + "\n" + line_10 + "\n" + line_11)
