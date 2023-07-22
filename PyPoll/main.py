import os
import csv

# Function to analyze the election data
def analyze_election_data(file_path):
    # Initialize variables to store data
    total_votes = 0
    candidate_votes = {}
    candidates_list = []

    # Read the CSV file and process the data
    with open(file_path, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        header = next(csvreader)  # Skip the header row
        for row in csvreader:
            total_votes += 1
            candidate_name = row[2]
            if candidate_name not in candidates_list:
                candidates_list.append(candidate_name)
                candidate_votes[candidate_name] = 0
            candidate_votes[candidate_name] += 1

    # Calculate the percentage of votes each candidate won
    percentage_votes = {}
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        percentage_votes[candidate] = (votes / total_votes) * 100

    # Find the winner based on popular vote
    winner = max(candidate_votes, key=candidate_votes.get)

    # Print the analysis to the terminal
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    for candidate in candidates_list:
        votes = candidate_votes[candidate]
        percentage = percentage_votes[candidate]
        print(f"{candidate}: {percentage:.3f}% ({votes})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

    # Export the analysis to a text file
    output_file = os.path.join("analysis", "election_results.txt")
    with open(output_file, "w") as txtfile:
        txtfile.write("Election Results\n")
        txtfile.write("-------------------------\n")
        txtfile.write(f"Total Votes: {total_votes}\n")
        txtfile.write("-------------------------\n")
        for candidate in candidates_list:
            votes = candidate_votes[candidate]
            percentage = percentage_votes[candidate]
            txtfile.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
        txtfile.write("-------------------------\n")
        txtfile.write(f"Winner: {winner}\n")
        txtfile.write("-------------------------\n")

# Run the analysis
file_path = os.path.join("Resources", "election_data.csv")
analyze_election_data(file_path)