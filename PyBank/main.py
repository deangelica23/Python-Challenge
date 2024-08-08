#Pybank

# In this Challenge, you are tasked with creating a Python script to analyze the financial records of your company. 

#import modules

import os

import csv

# need to input correct file path
csvpath = os.path.join('Resources', 'budget_data.csv')

#variables

total_months = 0
total_profit_losses = 0
profit_losses_changes = []
date = []
dates = []
profit_losses = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
   
    header = next(csvreader)

    for row in csvreader: 

# total number of month included in dataset
# The net total amount of "Profit/Losses" over the entire period

        total_profit_losses += int(row[1])
        profit_losses.append(int(row[1]))
        date.append(row [0])
        total_months += 1


for i , profit_loss in enumerate(profit_losses):
 
    if i < total_months - 1:

        difference = profit_losses [i + 1] - profit_loss
        profit_losses_changes.append(difference)
        dates.append(date [i+ 1])
        



#average change
average_change = round(sum(profit_losses_changes) / (total_months - 1), 2)



# The greatest increase in profits (date and amount) over the entire period

greatest_increase = max(profit_losses_changes)
greatest_increase_date = dates[profit_losses_changes.index(greatest_increase)]


# The greatest decrease in profits (date and amount) over the entire period

greatest_decrease = min(profit_losses_changes)
greatest_decrease_date = dates[profit_losses_changes.index(greatest_decrease)]



# print analysis to the terminal 

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# export to text file with results.

output_path = os.path.join('analysis', 'financial_analysis.txt')
with open(output_path, 'w') as file: 
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${total_profit_losses}\n")
    file.write(f"Average Change: ${average_change}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")




