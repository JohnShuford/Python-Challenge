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
    for (row) in csv_reader:
        line_count += 1
        if line_count > 1:
            #making sure the months aren't the same then finding the count
            if row[0] == row[0] + 1:
                month_count = month_count + 1
            #calculating the total
            total  = total + int(row[1])
    

    #creating the readout
    print("Financial Analysis")
    print("~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~")
    print(f"Total Months: {month_count}")
    print(f"Total: ${total}")
    print(f"Average Change: ${total/line_count}")
