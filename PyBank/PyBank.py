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

    #defining the buckets
    great_in_mnth = ""
    great_in_val = 0
    great_dec_mnth = ""
    great_dec_val = 0

    for (row) in csv_reader:
        line_count += 1
        if line_count > 1:
            #calculatint the month count
            month_count += 1
            #calculating the total
            total  = total + int(row[1])
            #Adding the profits in to a list
            profits.append(row[1])
    print(profits)
    great_in_val = max(profits)
    great_dec_val = min(profits)

    #creating the readout
    print("Financial Analysis")
    print("~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~")
    print(f"Total Months: {month_count}")
    print(f"Total: ${total}")
    print(f"Average Change: ${total/line_count}")
    print(f"Greatest Increase in Profits: {great_in_val}")
    print(f"Greatest Decrease in Prifits: {great_dec_val}")
