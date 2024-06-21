import pandas as pd
import os

directory = input("Enter the file path where the CSV files are located: ")

# List of all CSV files in the directory
csv_files = [i for i in os.listdir(directory) if i.endswith('.csv')]

# Available CSV files
print("Available CSV files:")
for i, filename in enumerate(csv_files, start=1):
    print(f"{i}. {filename}")

# Have user input the names of the CSV files they want to combine
selected_files = input("Enter the numbers (separated by commas) of the CSV files you want to combine: ")
selected_files = [int(i.strip()) - 1 for i in selected_files.split(",")]

# List to store dataframes
dataframes = []

# Loop through selected CSV files and read them into dataframes
for i in selected_files:
    filename = csv_files[i]
    filepath = os.path.join(directory, filename)
    df = pd.read_csv(filepath)  # Fixed indentation here
    dataframes.append(df)

# Concatenate all dataframes and create one combined dataframe
combined_df = pd.concat(dataframes)

valid_file_types = ['media', 'modelresults', 'observation', 'metadata']
file_type = input(f"Are these {', '.join(valid_file_types)} CSV files? ").strip().lower()
while file_type not in valid_file_types:
    print("Please enter a valid file type.")
    file_type = input(f"Are these {', '.join(valid_file_types)} CSV files? ").strip().lower()

# Have user give trip number
trip_number = int(input("Enter the trip number: "))

# Ensure trip number consistency
trip_number_str = f"{trip_number:02d}"

# Get year for CSV file name
year = input("Enter the year: ")

# Generate the filename
combined_filename = f"combined_{file_type}_{year}_trip{trip_number_str}.csv"

combined_df.to_csv(os.path.join(directory, combined_filename), index=False)

print("Combined CSV file has been created successfully.")

