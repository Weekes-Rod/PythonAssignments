import csv
import os

# Get the current script's directory
current_directory = os.path.dirname(os.path.abspath(__file__))

# Construct the file path to the CSV file
csv_file_path = os.path.join(current_directory, "Resources", "election_data.csv")

# Initialize variables
total_votes = 0
candidates = {}

# Read the CSV file
with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)

    # Skip the header row
    next(csv_reader)

    # Loop through each row in the CSV
    for row in csv_reader:
        # Increment total votes
        total_votes += 1

        # Extract candidate name from the row
        candidate_name = row[2]

        # Update candidate's vote count
        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            candidates[candidate_name] = 1

# Display the election results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# Loop through candidates and calculate percentages
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")

# Find the winner
election_winner = max(candidates, key=candidates.get)


print(f"Winner: {election_winner}")


# Save the results to a text file in the Analysis folder
analysis_directory = os.path.join(current_directory, "Analysis")
output_file_path = os.path.join(analysis_directory, "election_results.txt")

with open(output_file_path, 'w') as output_file:
    output_file.write("Election Results\n")
    
    output_file.write(f"Total Votes: {total_votes}\n")
    
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        output_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    
    output_file.write(f"Winner: {election_winner}\n")
    

print(f"Results saved to {os.path.join('Analysis', 'election_results.txt')}")

