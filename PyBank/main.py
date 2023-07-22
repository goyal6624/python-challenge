import csv

# Function to read the data from the CSV file
def read_budget_data(file_path):
    data = []
    with open(file_path, "r") as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Skip the header row
        for row in csvreader:
            data.append(row)
    return data

# Function to calculate the financial analysis
def calculate_financial_analysis(data):
    total_months = len(data)
    net_total = 0
    changes = []
    greatest_increase = 0
    greatest_decrease = 0
    greatest_increase_date = ""
    greatest_decrease_date = ""

    for i in range(total_months):
        date = data[i][0]
        profit_loss = int(data[i][1])
        net_total += profit_loss

        # Calculate the changes in profit/loss and store them in a list
        if i > 0:
            change = profit_loss - int(data[i - 1][1])
            changes.append(change)

            # Keep track of the greatest increase and decrease in profits
            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_date = date

            if change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_date = date

    # Calculate the average change in profit/loss
    average_change = sum(changes) / len(changes)

    return (
        total_months,
        net_total,
        average_change,
        greatest_increase,
        greatest_increase_date,
        greatest_decrease,
        greatest_decrease_date,
    )

# Function to print and export the results to a text file
def print_and_export_results(file_path, results):
    total_months, net_total, average_change, greatest_increase, greatest_increase_date, greatest_decrease, greatest_decrease_date = results

    # Format the output
    output = (
        f"Financial Analysis\n"
        f"----------------------------\n"
        f"Total Months: {total_months}\n"
        f"Total: ${net_total}\n"
        f"Average Change: ${average_change:.2f}\n"
        f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n"
        f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n"
    )

    # Print the output to the terminal
    print(output)

    # Export the results to a text file
    with open(file_path, "w") as txtfile:
        txtfile.write(output)

# Main function to run the analysis
def main():
    file_path = "Resources/budget_data.csv"
    data = read_budget_data(file_path)
    results = calculate_financial_analysis(data)
    print_and_export_results("analysis/financial_analysis.txt", results)

if __name__ == "__main__":
    main()