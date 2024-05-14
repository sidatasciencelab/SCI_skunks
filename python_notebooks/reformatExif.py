import pandas as pd
import subprocess, os

# Function to get serial number using exiftool
def get_serial_number(file_path):
    exiftool_output = subprocess.run(["exiftool", "-SerialNumber", file_path], capture_output=True, text=True)
    serial_number = exiftool_output.stdout.strip().split(": ")[-1]
    return serial_number
    

reformat_exifFilePath = input("Input path to csv file which contains exif data: \n")                 # Ask user for path to exif data     

reformat_exif_fileNameCSV = os.path.splitext(os.path.basename(reformat_exifFilePath))[0]
yesNoexif = input("Does this look correct? (yes/no) " + reformat_exifFilePath  + "\n")

if yesNoexif.lower() != "yes":                                                              # If user claims file path is incorrect, ask again    
  reformat_exifFilePath = input("Input path to csv file which contains exif data: \n")           
  yesNoexif = input("Does this look correct? (yes/no) " + reformat_exifFilePath + "\n")
  while yesNoexif.lower() != "yes":
    reformat_exifFilePath = input("Input path to csv file which contains exif data: \n")
    yesNoexif = input("Does this look correct? (yes/no) " + reformat_exifFilePath + "\n")
else: 
  reformat_exifFilePath = reformat_exifFilePath                                                           # If it passes have file equal to what user provided

reformat_exifPathExist = os.path.exists(reformat_exifFilePath)                                            # Verify that file path exists, output boolean

while reformat_exifPathExist != True:                                                            # If file path does not exist, have user input correct file path
  reformat_exifFilePath = input("The directory " + reformat_exifFilePath + " is an invalid directory, please enter a valid directory: \n")
  reformat_exifPathExist = os.path.exists(reformat_exifFilePath)  
print('reformatting exif csv file ...')
# Load the CSV file into a pandas DataFrame
csv_file = reformat_exifFilePath
df = pd.read_csv(csv_file)

# Iterate over the DataFrame rows and update serial numbers
for index, row in df.iterrows():
    file_path = row['SourceFile']
    serial_number = get_serial_number(file_path)
    df.at[index, 'SerialNumber'] = serial_number

# Save the modified DataFrame back to the CSV file
df.to_csv(csv_file, index=False)

print('exif csv file has been reformatted')
