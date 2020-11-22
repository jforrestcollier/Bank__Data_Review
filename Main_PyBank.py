# Pybank Python Exercise
import sys
import os
import csv

# Space out terminal output
print("\n\n")

# File path
path = "C:/Users/jforr/Rice Program/Class Materials/rice-hou-data-pt-10-2020-u-c/Homework/03-Python/Bank_Data_Review/Instructions/PyBank/Resources/budget_data.csv"

# Open Path
with open(path) as csvfile: 
    csvreader = csv.reader(csvfile,delimiter = ",")

    # Determine headers
    header = next(csvreader)
    
    # Define Variables
    uniq_month = []
    net = 0 
    pl = []

    # Unique months and net change iteration
    for row in csvreader:
        if row[0] not in uniq_month:
            uniq_month.append(row[0]) #unique months

        net = int(row[1]) + net # net P/L

        pl.append(row[1])

    # Define Variables
    change = [] 

    # average change iteration
    for i in range(1, len(pl)):
        value = int(pl[i]) - int(pl[i-1]) #row change
        change.append(value) #add to list
    
    # greatest_inc = change.minimum()
    # greatest_dec = change.maximum()
    pl_average = sum(change) / len(change) # calculate avarage change

    # greatest increase and decrease
    max_change = max(change) 
    min_change = min(change)
    max_change_month_index = int(change.index(max_change)) + 1
    min_change_month_index = int(change.index(min_change)) + 1
    max_change_month = uniq_month[max_change_month_index]
    min_change_month = uniq_month[min_change_month_index]


# Text file output
with open('C:/Users/jforr/Rice Program/Class Materials/rice-hou-data-pt-10-2020-u-c/Homework/03-Python/Bank_Data_Review/Instructions/PyBank/PyBank.txt', 'w') as text_file:
    # Print statements
    text_file.write("Financial Analysis\n")
    text_file.write("-----------------------\n")
    text_file.write(f'Total Months: {len(uniq_month)}\n')
    text_file.write(f'Total: ${net}\n')
    text_file.write(f'Average Change: ${round(pl_average)}\n')
    text_file.write(f'Greatest Increase in Profits: {max_change_month} (${max_change})\n')
    text_file.write(f'Greatest Increase in Profits: {min_change_month} (${min_change})')

