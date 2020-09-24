#importing the necessary libraries
import os
import csv
import statistics

#getting the path set
csv_path = os.path.join("budget_data.csv")

#opening the CSV file
with open (csv_path, mode = "r", newline="") as csv_file:
    #reading the file
    csv_reader = csv.reader(csv_file)

    #designating the header
    csv_header = next(csv_reader)

    #creating the counters
    month_count = 0
    total = 0
    profits = []
    avg_change = []
    
    #findig the counts
    for row in csv_reader:
        #calculatint the month count
        month_count += 1
        #calculating the total
        total  = total + int(row[1])
        #Adding the profits in to a list
        profits.append(int(row[1]))

    great_inc_mnth = " ."
    great_inc_val = max(profits)
    great_dec_mnth = " ."
    great_dec_val = min(profits)

    for row in csv_reader:
        if row[1] == "1170593": 
            great_inc_mnth = (str(row[0]))  

    print(great_inc_mnth)
    
    #creating a list with month to month change values
    for i in range(len(profits)-1):
       avg_change.append(profits[1+i]-profits[0+i])


    #creating the readout
    line_1 = "Financial Analysis"
    line_2 = "~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~"
    line_3 = f"Toatal Months: {month_count}"
    line_4 = f"Total: ${total}"
    line_5 = f"Average Change: ${round(statistics.mean(avg_change),2)}"
    line_6 = f"Greatest Increase in Profits: (${great_inc_val})"
    line_7 = f"Greatest Decrease in Profits: (${great_dec_val})"

print(line_1 + "\n" + line_2 + "\n" + line_3 + "\n" + line_4 + 
"\n" + line_5 + "\n" + line_6 + "\n" + line_7)

with open ('financial_analysis.txt', mode = "w") as text:
    text.writelines(line_1 + "\n" + line_2 + "\n" + line_3 + "\n" + line_4 + 
"\n" + line_5 + "\n" + line_6 + "\n" + line_7)
