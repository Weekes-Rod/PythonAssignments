import os
import csv

# Path to the budget_data.csv file
csv_path = os.path.join("Resources", "budget_data.csv")

# Lists to store data
dates = []
profits_losses = []

# Read the CSV file
with open(csv_path, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)  # Skip header row

    # Read data from CSV and store it in lists
    for row in csvreader:
        dates.append(row[0])
        profits_losses.append(int(row[1]))

# Calculate total number of months
total_months = len(dates)

# Calculate net total amount of "Profit/Losses"
net_total = sum(profits_losses)

# Calculate changes in "Profit/Losses" over the entire period
profit_changes = [profits_losses[i + 1] - profits_losses[i] for i in range(total_months - 1)]

# Calculate the average change
average_change = round(sum(profit_changes) / (total_months - 1), 2)

# Find the greatest increase and decrease in profits
max_increase = max(profit_changes)
max_decrease = min(profit_changes)

# Find the corresponding dates for greatest increase and decrease
max_increase_date = dates[profit_changes.index(max_increase) + 1]
max_decrease_date = dates[profit_changes.index(max_decrease) + 1]

# Display the results
print("Financial Analysis")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {max_increase_date} (${max_increase})")
print(f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})")

# Write the results to a text file
output_path = os.path.join("Analysis", "results.txt")
with open(output_path, "w") as txtfile:
    # Write results to the text file
    txtfile.write("Financial Analysis\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${net_total}\n")
    txtfile.write(f"Average Change: ${average_change}\n")
    txtfile.write(f"Greatest Increase in Profits: {max_increase_date} (${max_increase})\n")
    txtfile.write(f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})\n")
