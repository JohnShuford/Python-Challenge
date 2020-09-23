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
    avg_change = []

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
        if row[1] == 1170593: 
            great_inc_mnth = (row[0])  
    
    for i in range(len(profits)-1):
       avg_change.append(profits[0+i]-profits[1+i])


    print(avg_change)
    #print(profits)

    #creating the readout
    print("Financial Analysis")
    print("~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~")
    print(f"Toatal Months: {month_count}")
    print(f"Total: ${total}")
    print(f"Average Change: ${statistics.mean(avg_change)}")
    print(f"Greatest Increase in Profits: ({great_inc_val})")
    print(f"Greatest Decrease in Profits: ({great_dec_val})")
