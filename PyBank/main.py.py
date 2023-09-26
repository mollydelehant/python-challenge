import pandas as pd

# Load the CSV file
data = pd.read_csv('C:/Users/tpw3615/OneDrive - Northwestern University/Desktop/python-challenge/PyBank/Resources/budget_data.csv')

# Convert the "Date" column to datetime objects with the specified format
data['Date'] = pd.to_datetime(data['Date'], format='%b-%y')

# Calculate the total number of unique months
total_months = len(data['Date'].dt.to_period('M').unique())

# Calculate the net total amount of "Profit/Losses"
net_total = data['Profit/Losses'].sum()

# Calculate the changes in "Profit/Losses" over the entire period
data['Profit/Loss Change'] = data['Profit/Losses'].diff()

# Calculate the average of those changes
average_change = data['Profit/Loss Change'].mean()

# Calculate the greatest increase in profits
max_increase = data['Profit/Loss Change'].max()
max_increase_date = data.loc[data['Profit/Loss Change'] == max_increase, 'Date'].values[0]

# Calculate the greatest decrease in profits
max_decrease = data['Profit/Loss Change'].min()
max_decrease_date = data.loc[data['Profit/Loss Change'] == max_decrease, 'Date'].values[0]

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
print(f"{pd.to_datetime(max_increase_date).strftime('%b-%y')}: ${max_increase:,.2f}")
print("-------------------------")
print("Greatest decrease in profits (date and amount):")
print("-------------------------")
print(f"{pd.to_datetime(max_decrease_date).strftime('%b-%y')}: ${max_decrease:,.2f}")
print("-------------------------")
