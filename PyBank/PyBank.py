#importing the necessary libraries
import csv
import statistics

#opening the CSV file
with open ('budget_data.csv', mode = "r", newline="") as csv_file:
    #reading the file
    csv_reader = csv.reader(csv_file)

    #creating the counters
    month_count = 0
    total = 0
    profits = []
    avg_change = []

    #designating the header
    csv_header = next(csv_reader)
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
        if row[1] == great_inc_val: 
            great_inc_mnth = (row[0])  

    print(great_inc_mnth)
    
    #creating a list with month to month change values
    for i in range(len(profits)-1):
       avg_change.append(profits[0+i]-profits[1+i])


    #creating the readout
    print("Financial Analysis")
    print("~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~")
    print(f"Toatal Months: {month_count}")
    print(f"Total: ${total}")
    print(f"Average Change: ${round(statistics.mean(avg_change),2)}")
    print(f"Greatest Increase in Profits: ({great_inc_val})")
    print(f"Greatest Decrease in Profits: ({great_dec_val})")
