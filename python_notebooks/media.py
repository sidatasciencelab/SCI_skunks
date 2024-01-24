# -*- coding: utf-8 -*-

#sudo OPENBLAS_CORETYPE=ARMV8 python3 /home/pi/Downloads/SCI_skunks-main/python_notebooks/deploymediaobs.py

### Deploy Media Observations

import pandas as pd 
import json, datetime, os


exifFilePath = input("Input path to csv file which contains exif data: \n")

yesNo = input("Does this look correct? " + exifFilePath  + "\n")

if yesNo.lower() != "yes":
  exifFilePath = input("Input path to csv file which contains exif data: \n")
  yesNo = input("Does this look correct? " + exifFilePath + "\n")
  while yesNo.lower() != "yes":
    exifFilePath = input("Input path to csv file which contains exif data: \n")
    yesNo = input("Does this look correct? " + exifFilePath + "\n")
else: 
  exifFilePath = exifFilePath

exifPathExist = os.path.exists(exifFilePath)

while exifPathExist != True:
  exifFilePath = input("The directory " + exifFilePath + " is an invalid directory, please enter a valid directory: \n")
  exifPathExist = os.path.exists(exifFilePath)

#taking in a valid Model results path
modelPath = input("Input path to csv file which contains model classification data: \n")

yesNo = input("Does this look correct? " + modelPath  + "\n")

if yesNo.lower() != "yes":
  modelPath = input("Input path to csv file which contains model classification data: \n")
  yesNo = input("Does this look correct? " + modelPath + "\n")
  while yesNo.lower() != "yes":
    modelPath = input("Input path to csv file which contains model classification data: \n")
    yesNo = input("Does this look correct? " + modelPath  + "\n")
else: 
  modelPath = modelPath

modelPathExist = os.path.exists(modelPath)

while modelPathExist != True:
  modelPath = input("The directory " + modelPath + " is an invalid directory, please enter a valid directory: \n")
  modelPathExist = os.path.exists(modelPathExist)

#/content/2022_testLoc_testCamNum_testTripNum.csv
#/content/model_Results_2022_testLoc_testCamNum_testTripNum.csv
data = pd.read_csv(exifFilePath) #change data to exifData
modelData = pd.read_csv(modelPath)

# add chunk here that filters TriggerMode column to only include motion detection
#samp = pd.read_csv("/content/data.csv")

"""###Deployments.csv """

#ask for camera_loc & cam_postion 

#set up as independent varibles 
cameraID = (input("Please enter Camera ID: ")).upper()
yesNo = input("Does this look correct? " + cameraID  + "\n")

while yesNo.lower() != "yes":
  cameraID = (input("Please enter Camera ID: ")).upper()
  yesNo = input("Does this look correct? " + cameraID + "\n")


cameraLoc = (input("Please enter Camera Loc. Name: ")).upper()
yesNo = input("Does this look correct? " + cameraLoc  + "\n")


while yesNo.lower() != "yes":
  cameraLoc = (input("Please enter Camera Loc. Name: ")).upper()
  yesNo = input("Does this look correct? " + cameraLoc + "\n")

#deploymentID -> cameraID+cameraLoc

deploymentID = cameraID + "_" + cameraLoc

#locationID -> cameraID

locationID = cameraID

#locationName -> cameraLoc
locationName = cameraLoc

#longitude -> should be float with 5 decimal places 
  #example: 52.70442 -> [52, 70442]

longitude = float(input("Please enter longitude with 5 decimal place accuracy: "))
while (len(str(longitude).split(".")[1]) != 5):
  longitude = float(input("Please enter longitude with 5 decimal place accuracy: "))


#latitude -> should be float with 5 decimal places 
  #example: 52.70442

latitude = float(input("Please enter latitude with 5 decimal place accuracy: "))
while (len(str(latitude).split(".")[1]) != 5):
  latitude = float(input("Please enter latitude with 5 decimal place accuracy: "))

#start -> date of oldest picture in csv file
start = data.sort_values(by=["DateTimeOriginal"]).DateTimeOriginal[0]

#end -> date of newest picture in csv file
end = data.sort_values(by=["DateTimeOriginal"]).iloc[-1].DateTimeOriginal


#cameraID ->  df['A'].unique()
cameraID =  cameraID

#cameraModel -> data.model.unique() #should be a single value since its all the same camera
cameraModel = data[~data['Model'].isnull()].Model.unique()[0]

#camera interval -> should be a static for every single camera

cameraInterval = 0

#baitused -> static no for all cameras

baitused = "None"

#_id -> empty 
_id = ""

#comments -> static empty column 

#save this as deployments+name of exifdata (without extension) +.csv
  #example: deployments_2022_UCSB11_11A_02.csv

fileNameCSV = (exifFilePath.split("/")[-1]).split(".")[0]

#creating dictionary with appropriate structure
deploymentContent = {"deploymentID" : [deploymentID],
                     "locationID" : [locationID], 
                     "locationName" : [locationName], 
                     "longitude" : [longitude], 
                     "latitude" : [latitude], 
                     "start" : [start],
                     "end" : [end],
                     "cameraID" : [cameraID], 
                     "cameraModel" : [cameraModel], 
                     "cameraInterval" : [cameraInterval], 
                     "baitused": [baitused],
                     "_id" : ["NaN"]}

csvName = "deployments_" + str(fileNameCSV) + ".csv"

deploymentPD = pd.DataFrame.from_dict(deploymentContent)

deploymentPD.to_csv(csvName, sep=',', index=False)

print("Deployments file for this camera has been created and saved in the current working directory under'" + csvName + "'")

"""###Media.csv

"""
#ask for camera_loc & cam_postion 

#set up as independent varibles 
cameraID = data.SerialNumber
yesNo = input("Does this serial number look correct? " + cameraID  + "\n")

while yesNo.lower() != "yes":
  cameraID = (input("Please enter camera serial number: ")).upper()
  yesNo = input("Does this look correct? " + cameraID + "\n")

cameraLoc = (input("Please enter camera location name: ")).upper()
yesNo = input("Does this look correct? " + cameraLoc  + "\n")

while yesNo.lower() != "yes":
  cameraLoc = (input("Please enter camera location name: ")).upper()
  yesNo = input("Does this look correct? " + cameraLoc + "\n")

deploymentID = cameraLoc + "_" + cameraID

locationID = cameraID

locationName = cameraLoc

mediaID = data.FileName 

sequenceID = data.EventNumber

#captureMethod -> static column where all values => 
captureMethod = "Motion detection"

#filePath -> data.SourceFile
filePath = data.Directory

#fileName -> data.FileName
fileName = data.FileName

#fileMediatype -> data.MIMEType
fileMediatype = data.MIMEType

#exifData -> exiftool data dump 
#creating a column that contains the exif data of each entry. 
exifList = []
for i in data.index:
    exifList.append(data.loc[i].to_json( orient = "split", ))

#comments -> input("Are there anycomments present on the data sheet? ")

yesNo = input("Any Extra comments that you would like to add; you would want to enter field notes here: ")

if yesNo.lower() != "no":
  comments = input("input comment: ")
  print(comments)
  correct = input("does this look correct (Yes/No)? ")
  while correct.lower() != "yes":
    comments = input("input comment: ")
    print(comments)
    correct = input("does this look correct (Yes/No)? ")
else: 
  comments = ""
  
#timeStamp current time for all 

timeStamp = datetime.datetime.utcnow().isoformat()

#fileName already set earlier.
#fileName = (exifFilePath.split("/")[-1]).split(".")[0]

#creating dictionary with appropriate structure

mediaContent=pd.concat([mediaID,filePath, fileMediatype],axis=1) #concat series column 

dict = {'FileName': 'mediaID',
        'Directory': 'filePath',
        'MIMEType': 'fileMediatype'}
 
# call rename () method
mediaContent.rename(columns=dict,
          inplace=True)

#addind static columns 
timeStamp = datetime.datetime.utcnow().isoformat()

mediaContent['deploymentID'] = pd.Series([deploymentID for x in range(len(mediaContent.index))])

mediaContent['sequenceID'] = pd.Series(["seq1" for x in range(len(mediaContent.index))])

mediaContent['captureMethod'] = pd.Series(["Motion detection" for x in range(len(mediaContent.index))])

mediaContent['comments'] = pd.Series([comments for x in range(len(mediaContent.index))])

mediaContent['timeStamp'] = pd.Series([timeStamp for x in range(len(mediaContent.index))])

mediaContent['fileName'] = data.SourceFile

mediaContent['favourite'] = pd.Series(["" for x in range(len(mediaContent.index))])

mediaContent['_id'] = pd.Series(["" for x in range(len(mediaContent.index))])




mediaContent['exifData'] = exifList

#reording dataframe 


order = ["mediaID", "deploymentID", "sequenceID", "captureMethod", "timeStamp", "filePath", "fileName", "fileMediatype", "exifData", "favourite", "comments", "_id"]

mediaContent = mediaContent[order]

csvName = "media_" + str(fileNameCSV) + ".csv"

#csvName
mediaContent.to_csv(csvName, sep=',', index=False)

print("Media file for this camera has been created and saved in the current working directory under'" + csvName + "'")

data.Directory
