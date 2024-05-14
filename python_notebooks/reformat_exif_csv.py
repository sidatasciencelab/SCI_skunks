import pandas as pd
import subprocess

# Function to get serial number using exiftool
def get_serial_number(file_path):
    exiftool_output = subprocess.run(["exiftool", "-SerialNumber", file_path], capture_output=True, text=True)
    serial_number = exiftool_output.stdout.strip().split(": ")[-1]
    return serial_number

# Load the CSV file into a pandas DataFrame
csv_file = "/media/zachary/SDCARD/DCIM/metaData_2023_1_05_5A.csv"
df = pd.read_csv(csv_file)

# Iterate over the DataFrame rows and update serial numbers
for index, row in df.iterrows():
    file_path = row['SourceFile']
    serial_number = get_serial_number(file_path)
    df.at[index, 'SerialNumber'] = serial_number

# Save the modified DataFrame back to the CSV file
df.to_csv(csv_file, index=False)
