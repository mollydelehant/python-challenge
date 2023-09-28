# Load the CSV file
data = []
with open('C:/Users/tpw3615/OneDrive - Northwestern University/Desktop/python-challenge/PyBank/Resources/budget_data.csv', 'r') as file:
    lines = file.readlines()
    header = lines[0].strip().split(',')
    for line in lines[1:]:
        values = line.strip().split(',')
        data.append({
            header[0]: values[0],
            header[1]: int(values[1])
        })

# Convert the "Date" column to datetime objects with the specified format
for entry in data:
    entry['Date'] = entry['Date']  # No need to convert in basic Python

# Calculate the total number of unique months
unique_months = set(entry['Date'] for entry in data)
total_months = len(unique_months)

# Calculate the net total amount of "Profit/Losses"
net_total = sum(entry['Profit/Losses'] for entry in data)

# Calculate the changes in "Profit/Losses" over the entire period
profit_losses_changes = [entry['Profit/Losses'] for entry in data]
profit_losses_changes.insert(0, 0)  # Insert a 0 for the first month
for i in range(1, len(profit_losses_changes)):
    profit_losses_changes[i] -= profit_losses_changes[i - 1]

# Calculate the average of those changes
average_change = sum(profit_losses_changes) / (len(profit_losses_changes) - 1)  # Exclude the initial 0

# Calculate the greatest increase in profits
max_increase = max(profit_losses_changes)
max_increase_index = profit_losses_changes.index(max_increase)
max_increase_date = data[max_increase_index]['Date']

# Calculate the greatest decrease in profits
max_decrease = min(profit_losses_changes)
max_decrease_index = profit_losses_changes.index(max_decrease)
max_decrease_date = data[max_decrease_index]['Date']

print("Total number of months:", total_months)
print("-------------------------")
print("Net total amount of 'Profit/Losses': ${:,.2f}".format(net_total))
print("-------------------------")
print("Changes in 'Profit/Losses' over the entire period")
print("-------------------------")
print("Average of those changes: ${:,.2f}".format(average_change))
print("-------------------------")
print("Greatest increase in profits (date and amount):")
print("-------------------------")
print(f"{max_increase_date}: ${max_increase:,.2f}")
print("-------------------------")
print("Greatest decrease in profits (date and amount):")
print("-------------------------")
print(f"{max_decrease_date}: ${max_decrease:,.2f}")
print("-------------------------")