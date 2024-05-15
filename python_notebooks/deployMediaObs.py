# -*- coding: utf-8 -*-

#sudo OPENBLAS_CORETYPE=ARMV8 python3 /home/pi/Downloads/SCI_skunks-main/python_notebooks/deploymediaobs.py

### Deploy Media Observations

# ensure environment has pandas and datetime, in my case I had to use pip install pandas and pip install  
# datetime to run the remaining code in my visual studio code on my windows computer 

import pandas as pd 
import json, datetime, os


exifFilePath = input("Input path to csv file which contains exif data: \n")                 # Ask user for path to exif data     

exif_fileNameCSV = os.path.splitext(os.path.basename(exifFilePath))[0]
yesNoexif = input("Does this look correct? (yes/no) " + exifFilePath  + "\n")

if yesNoexif.lower() != "yes":                                                              # If user claims file path is incorrect, ask again    
  exifFilePath = input("Input path to csv file which contains exif data: \n")           
  yesNoexif = input("Does this look correct? (yes/no) " + exifFilePath + "\n")
  while yesNoexif.lower() != "yes":
    exifFilePath = input("Input path to csv file which contains exif data: \n")
    yesNoexif = input("Does this look correct? (yes/no) " + exifFilePath + "\n")
else: 
  exifFilePath = exifFilePath                                                           # If it passes have file equal to what user provided

exifPathExist = os.path.exists(exifFilePath)                                            # Verify that file path exists, output boolean

while exifPathExist != True:                                                            # If file path does not exist, have user input correct file path
  exifFilePath = input("The directory " + exifFilePath + " is an invalid directory, please enter a valid directory: \n")
  exifPathExist = os.path.exists(exifFilePath)


modelPath = input("Input path to csv file which contains model classification data: \n") # Ask user for path to exif data

model_fileNameCSV = os.path.splitext(os.path.basename(modelPath))[0]
yesNomodel = input("Does this look correct? (yes/no) " + modelPath  + "\n")

if yesNomodel.lower() != "yes":                                                              # If user claims file path is incorrect, ask again
  modelPath = input("Input path to csv file which contains model classification data: \n")
  yesNomodel = input("Does this look correct? (yes/no) " + modelPath + "\n")
  while yesNomodel.lower() != "yes":
    modelPath = input("Input path to csv file which contains model classification data: \n")
    yesNomodel = input("Does this look correct? (yes/no) " + modelPath  + "\n")
else: 
  modelPath = modelPath                                                                 # If it passes have file equal to what user provided

modelPathExist = os.path.exists(modelPath)                                              # Verify that file path exists, output boolean

while modelPathExist != True:                                                           # If file path does not exist, have user input correct file path
  modelPath = input("The directory " + modelPath + " is an invalid directory, please enter a valid directory: \n")
  modelPathExist = os.path.exists(modelPathExist)

exifData = pd.read_csv(exifFilePath)                                                    # Read in csv file provided at file path as a dataframe named exifData                                     
modelData = pd.read_csv(modelPath)                                                      # Read in csv file provided at file path as a dataframe named modelData

exifData = exifData[exifData['TriggerMode'] == 'Motion Detection']                      #filter "TriggerMode" column so it only contains "Motion Detection" rows

"""###Deployments.csv """

print("The deployment file should be a CSV file that is manually updated, accessible via Trello or GitHub.")

acknowledge = input("Please acknowledge by typing 'yes' to continue: ")

if acknowledge.lower() != "yes":
    print("You must acknowledge the message to continue.")
    while acknowledge.lower() !="yes":
      input("Please acknowledge by typing 'yes' to continue: ")
else: print("Thank you, you will now be prompted to create the media file.")


"""###Media.csv
"""
# Ask the user to input comments
yesnocomment = input("Any comments you would like to leave in this media file? (yes/no): \n")

if yesnocomment.lower() != "no":
  mediaComments = input("Input comment: \n")
  correct = input("Does this look correct (yes/no)? " + mediaComments + "\n")
  while correct.lower() != "yes":
    mediaComments = input("Input comment: \n")
    correct = input("Does this look correct (yes/no)? " + mediaComments + "\n")
else: 
  mediaComments = ""

#Ask the user to input the locationID
locationID = input("Give the location ID for this media file (i.e. 5A): \n")
yesNolocation = input("Does this look correct? (yes/no) " + locationID + "\n")

if yesNolocation.lower() != "yes":                                                              # If user claims file path is incorrect, ask again
  locationID = input("Give the location ID for this media file (i.e. 5A): \n")
  yesNolocation = input("Does this look correct? (yes/no) " + locationID + "\n")
  while yesNolocation.lower() != "yes":
    locationID = input("Give the location ID for this media file (i.e. 5A): \n")
    yesNolocation = input("Does this look correct? (yes/no) " + locationID  + "\n")
else: 
  locationID = locationID

#create column for future exifData column 
  
# Create a column containing all the information in JSON format 
exifList = []                                                                                   # create empty list                                                               # empty list 

for _, row in exifData.iterrows():                                                              # skip index column, interate through rows 
    exif_json = row.to_dict()                                                                   # turn each row into dictionary 
    exifList.append(json.dumps(exif_json))                                                      # turn the contents of the dictionary into the JSON format

def convert_to_iso8601(date_str):
    date_time_parts = date_str.split(' ')                                                       # Split date into two parts based on space between date and time 
    date_part = date_time_parts[0]                                                              # Get the date part which is the first in the list
    time_part = date_time_parts[1]                                                              # Get the time part which is the second in the list 
    iso8601_date = date_part.replace(':', '-') + 'T' + time_part + '-08:00'                     # concatenate parts of the previous string with new strings to get it in the right time format 
    return iso8601_date

ISO8601Date = exifData['DateTimeOriginal'].apply(convert_to_iso8601)

# Creating new DataFrame
mediaContent = pd.DataFrame({
    'mediaID': exifData['FileName'].str.replace('.JPG', ''),
    'deploymentID': locationID + "_" + exifData['SerialNumber'],
    'captureMethod': exifData['TriggerMode'],
    'timestamp': ISO8601Date,                        #current time stamp
    'filePath': "/store/public/ocio_dsl/ucsb_skunk_data/ucsb_skunk_images/" + exifData['FileName'],
    'filePublic': "true", 
    'fileName': exifData['FileName'],
    'fileMediatype': exifData['MIMEType'],
    'exifData': exifList,
    'mediaComments': [mediaComments] * len(exifData)                                              # Repeat the same comment for each row
})

mediaorder = ["mediaID", "deploymentID", "captureMethod", "timestamp", "filePath", "filePublic", "fileName",
         "fileMediatype", "exifData", "mediaComments"]
mediaContent = mediaContent[mediaorder]

mediacsvName = "media_" + str(exif_fileNameCSV) + ".csv"
mediaContent.to_csv(mediacsvName, sep=',', index=False)

print("Media file has been created and saved as '" + mediacsvName + "' in the current working directory.")  

acknowledge_media = input("Please acknowledge by typing 'yes' to continue: ")

if acknowledge_media.lower() != "yes":
    print("You must acknowledge the message to continue.")
    while acknowledge_media.lower() !="yes":
      input("Please acknowledge by typing 'yes' to continue: ")
else: print("Thank you, you will now be prompted to create the observation file.")

"""###Observation.csv
"""

# Creating new observation DataFrame

yesnocomment = input("Any comments you would like to leave in this observation file? (yes/no): \n")

if yesnocomment.lower() != "no":
  obsComments = input("Input comment: \n")
  correct = input("Does this look correct (yes/no)? " + obsComments + "\n")
  while correct.lower() != "yes":
    obsComments = input("Input comment: \n")
    correct = input("Does this look correct (yes/no)? " + obsComments + "\n")
else: 
  obsComments = ""

def pad_with_zeros(x):
    return str(x).zfill(5)

observationContent = pd.DataFrame({
    'observationID': exifData['FileName'].str.split('_').str[:4].str.join('_') + "_obs",
    'deploymentID': locationID + "_" + exifData['SerialNumber'],
    'mediaID': exifData['FileName'].str.replace('.JPG', ''),
    'eventID': exifData['FileName'].str.split('_').str[:4].str.join('_') + '_evt_' + exifData['EventNumber'].astype(str).apply(pad_with_zeros),
    'eventStart': ISO8601Date,
    'eventEnd': ISO8601Date,
    'observationLevel': 'media',
    'count': 'NA', 
    'classificationMethod': 'machine',
    'observationComments': [obsComments] * len(exifData)
})

modelData['imageName'] = modelData['imageName'].str.replace('.JPG', '')

observationContent_joined = pd.merge(observationContent, modelData, left_on = 'mediaID', right_on = 'imageName', how = 'left')

observationContent_joined.drop(columns=['imageName', 'accuracy'], inplace = True)

observationContent_joined.rename(columns = {'imageLabel': 'observationType'}, inplace = True)

observationContent_joined.rename(columns = {'classificationTimeStamp': 'classificationTimestamp'}, inplace = True)

obsorder = ['observationID', 'deploymentID', 'mediaID','eventID', 'eventStart', 'eventEnd',
            'observationLevel', 'observationType','count','classificationMethod', 'classificationTimestamp', 'observationComments']
observationContent_joined = observationContent_joined[obsorder]

count_values = range(1, len(observationContent_joined) + 1)

observationContent_joined['observationID'] += '_' + pd.Series(count_values).astype(str).apply(pad_with_zeros)

observationcsvName = "observation_" + str(exif_fileNameCSV) + ".csv"
observationContent_joined.to_csv(observationcsvName, sep=',', index=False)

print("Observation file has been created and saved as '" + observationcsvName + "' in the current working directory.")  

acknowledge_observation = input("Please acknowledge by typing 'yes' to continue: ")
  
if acknowledge_observation.lower() != "yes":
    print("You must acknowledge the message to continue.")
    while acknowledge_observation.lower() !="yes":
      input("Please acknowledge by typing 'yes' to continue: ")
else: print("Thank you, you have created the observation file.")


