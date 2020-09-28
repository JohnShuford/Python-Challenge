#importing the necessary libraries
import os
import csv

#getting the path set
csv_path = os.path.join("Resources", "budget_data.csv")

#opening the CSV file
with open (csv_path, mode = "r", newline="") as csv_file:
    #reading the file
    csv_reader = csv.reader(csv_file)

    #designating the header
    csv_header = next(csv_reader)

    #creating the lists ans setting the first values
    net_change_list = []
    great_inc = ["",0]
    great_dec = ["",1000000]
    first_row =  next(csv_reader)
    prev_net = int(first_row[1])
    month_count = 1
    total = int(first_row[1])

    #findig the counts
    for row in csv_reader:
        #calculatint the month count
        month_count += 1
        #calculating the total
        total  = total + int(row[1])

        #track the net change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list.append(net_change)

        #greatest increase1
        if net_change > great_inc[1]:
            great_inc[0] = row[0]
            great_inc[1] = net_change

        #greatest decrease
        if net_change < great_dec[1]:
            great_dec[0] = row[0]
            great_dec[1] = net_change

        #average change 
        avg_change_num = round((sum(net_change_list))/(len(net_change_list)),2)

#creating the readout
line_1 = "Financial Analysis"
line_2 = "~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~"
line_3 = f"Toatal Months: {month_count}"
line_4 = f"Total: ${total}"
line_5 = f"Average Change: ${avg_change_num}"
line_6 = f"Greatest Increase in Profits: {great_inc[0]} (${great_inc[1]})"
line_7 = f"Greatest Decrease in Profits: {great_dec[0]} (${great_dec[1]})"

#printing the lines in the terminal
print(line_1 + "\n" + line_2 + "\n" + line_3 + "\n" + line_4 + \
"\n" + line_5 + "\n" + line_6 + "\n" + line_7)

#setting the relative path for the text file
txt_path = os.path.join("Analysis", "financial_analysis.txt")

#creating the text file
with open (txt_path, mode = "w") as text:
    text.writelines(line_1 + "\n" + line_2 + "\n" + line_3 + "\n" + line_4 + \
"\n" + line_5 + "\n" + line_6 + "\n" + line_7)
