
import os
import csv

os.getcwd()

path = os.path.join(os.getcwd(), "Resources", "budget_data.csv")
print(path)

total_months = []
total_profit = []
monthly_profit_change = []

# Open File in Read mode
with open(path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    #Skip the header row
    header = next(csvreader)
    #Loop through the rows
    for row in csvreader:
        #Append total months & profit variables to thier corresponding lists
        total_months.append(row[0])
        total_profit.append(int(row[1]))

    #Loop through the profits to get monthly change in profits
    for i in range(len(total_profit) - 1):
        #Difference between months & append to monthly profit change
        monthly_profit_change.append(total_profit[i + 1] - total_profit[i])

# Get the greatest increase & decrease (date & amount)
greatest_increase = max(monthly_profit_change)
greatest_decrease = min(monthly_profit_change)

# Assign Max & Min to thier month
greatest_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
greatest_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1

# Print Statements
print("Financial Analysis")
print("--------------------------")
print(f"Total Months:  {len(total_months)}")
print(f"Total:  ${sum(total_profit)}")
print(f"Average Change:  {round(sum(monthly_profit_change) / len(monthly_profit_change),2)}")
print(f"Greatest Increase In Profits:  {total_months[greatest_increase_month]}(${(str(greatest_increase))})")
print(f"Greatest Decrease In Profits:  {total_months[greatest_decrease_month]}(${(str(greatest_decrease))})")

# Output the Files into Text
output_file = os.path.join(os.getcwd(), "Analysis", "budget_data.txt")

with open(output_file, "w") as datafile:
    # Write the commands
    datafile.write("Financial Analysis")
    datafile.write("--------------------------")
    datafile.write(f"Total Months:  {len(total_months)}")
    datafile.write(f"Total:  ${sum(total_profit)}")
    datafile.write(f"Average Change:  {round(sum(monthly_profit_change) / len(monthly_profit_change),2)}")
    datafile.write(f"Greatest Increase In Profits:  {total_months[greatest_increase_month]}(${(str(greatest_increase))})")
    datafile.write(f"Greatest Decrease In Profits:  {total_months[greatest_decrease_month]}(${(str(greatest_decrease))})")

