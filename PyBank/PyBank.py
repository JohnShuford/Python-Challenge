#importing the necessary libraries
import os
import csv
import statistics

#opening the CSV file
with open ('budget_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    #creating the counters
    line_count = 0
    month_count = 0
    total = 0
    profits = []

    for (row) in csv_reader:
        line_count += 1
        if line_count > 1:
            #calculatint the month count
            month_count += 1
            #calculating the total
            total  = total + int(row[1])
            #Adding the profits in to a list
            profits.append(int(row[1]))
    line_count_2 = 0
    great_inc_mnth = " ."
    great_inc_val = max(profits)
    great_dec_mnth = " ."
    great_dec_val = min(profits)
    for row in csv_reader:
        line_count_2 += 1
        if line_count_2 > 1:
            if row[1] == str(max(profits)): 
                great_inc_mnth = (row[0])  
    
    print(great_inc_mnth)
    
    #print(profits)

    #creating the readout
    print("Financial Analysis")
    print("~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~")
    print(f"Toatal Months: {month_count}")
    print(f"Total: ${total}")
    print(f"Average Change: ${total/line_count}")
    print(f"Greatest Increase in Profits: {great_inc_val}")
    print(f"Greatest Decrease in Profits: {great_dec_val}")
