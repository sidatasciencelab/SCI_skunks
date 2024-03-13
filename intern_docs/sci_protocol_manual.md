---
title: "SCI Protocol Skunk Crew Manual"
author: "Richard Montes Lemus"
date: "February 28, 2024"
---
# Introduction
The Island Spotted Skunk Monitoring Project is a collaborative project between the Smithsonian Data Science Lab and the UCSB Office of Education Partnerships. This manual outlines the steps Skunk Crew members should follow to ensure an efficient workflow, from the pre-trip preparations to final data submission.

## Pre-Trip Preparations
### Coordinators' Communication
- Review the email from coordinators containing essential trip details, including dates, information packets, packing lists, and itineraries.
### Print List Review
- Check the print list on Trello and GitHub for necessary prints.
- Print and compile required documents for the trip (OEP prints for free).
- Update protocols as needed (e.g., update datasheet if a camera was replaced last trip).
### Food and Gear Preparation
- Collect and store food in designated bins and boxes.
- Pack necessary gear into boxes for transportation.
### Task Assignments
- Create a task list splitting up responsibilities amongst participants, such as transporting supplies, checking in with IPCO (Boat to Santa Cruz Island), weighing items, and loading IPCO.

## On-Site Tasks
### Ventura Harbor Pier
- Arrival and completion of designated tasks at the pier.
### Prisoners Bay, Santa Cruz Island
- Unloading items and transportation to the field site.
### Field Site Preparation
- Organize rooms and store food and gear accordingly.

## Field Data Collection
### Camera Trap Setup
- Prepare the skunk box and folder with necessary items for fieldwork tasks. See [Skunk Box and Folder Checklist](#checklist).
- Follow detailed steps for collecting data at camera trap sites, replacing batteries, and documenting field notes and metadata on data sheets.
- See [Updated Camera Trap Data Collection Protocol](#protocol). 

## Data Processing
- Process collected SD cards using the mass rename script and machine learning model script. See [Mass Rename and Model Instructions](#massandmodel). 
- Generate CSV files from both scripts and compile relevant field notes and metadata from the data sheets for each camera trap site - they will be used in Post-Trip Procedures: Data Management.
### Inventory Update
- Update inventory lists based on field requirements before leaving the island.

## Post-Trip Procedures
### Return to UCSB
- Transportation of equipment, food, and secure data back to UCSB.
### Data Management
- Store metadata sheets and data safely.
- Compilation and organization of CSV files using tabular manipulation and binding, including mass rename script results, model outcomes, and field notes (from CSV file that will be created and manually filled in for metadata datasheet field notes and camera set notes).
### Data Submission
- Format CSV files to Camtrap DP standards.
- Store CSV files and images on a hard drive.
- Send data to the Smithsonian's Hydra computer using Globus from the hard drive.
- Upload metadata sheets and standardized CSV files to GitHub.
- Take a picture of metadata sheets and upload to GitHub or somewhere else safe.
- Store metadata datasheets and hard drive somewhere safe.

# Conclusion
The completion of these steps ensures the efficient collection, processing, and submission of data for the Island Spotted Skunk Monitoring Project.


# Skunk Box and Folder Checklist <a name="checklist"></a>
## Box Prep:
- [ ] Zip ties
- [ ] First aid kit
- [ ] Flagging tape
- [ ] Trauma pack
- [ ] Zip bag for used batteries
- [ ] Bungee cords
- [ ] Extra camera
- [ ] Straps for trap
- [ ] GPS
- [ ] Ensure Camera Points are in GPS. If not, get a new GPS or transfer the points from another GPS in settings. Check battery charge.
- [ ] 24 batteries per point (Each point has two cameras and each camera requires 12 batteries. Point 1 only has one camera)
- [ ] Gardening gloves
- [ ] Cutting shears
- [ ] Poison ivy treatment (Tecnu)
- [ ] Shovel

## Folder Prep:
- [ ] Dry erase marker
- [ ] Compass
- [ ] 2 desiccant packets per point + 3 extra
- [ ] 2 SD cards per point + two extra
- [ ] Brushes
- [ ] Paper clips
- [ ] Pens and pencils for writing
- [ ] Map of the Island
- [ ] Necessary printed protocols and procedures
- [ ] Blown up MP map
- [ ] Camera manual


# Updated Camera Trap Data Collection Protocol <a name="protocol"></a>

# Disclaimer
This Protocol is still in the works, more steps are soon to be added.

## Camera Trap Data Collection Protocol
(Note there are multiple different types of cameras, some will have slightly different prompts)

### Approaching Camera Trap:
- Take a mugshot.
- With a dry erase marker, fill in Camera #: UCSBCameraID (e.g., “UCSB02”) and the date on the SCI Spotted Skunk folder’s laminated mugshot paper.
- Approach the camera trap and ensure the mugshot is visible to it and in its range.
- If the camera light blinks when you approach, the batteries have not died yet, and it will take the mugshot.

### Replacing Batteries and Collecting Metadata:
- Assign data recorder and camera trap handler:
  - Camera trap handler will read camera trap metadata to data recorder, and data recorder will track it on the metadata sheet.
- Camera trap handler:
  - Open camera and read battery charge status.
  - Replace batteries and store old batteries in used batteries ziplock.
  - Read new battery charge status.
  - Navigate to Battery Type.
  - Read battery type.
  - Navigate to Status/About.
  - Read # of images on card.
  - Read time (Change if incorrect, Check Manual).
  - Read date.
  - Read version number.
  - Read serial number.
  - Navigate to Change Setup and Navigate to Motion.
  - Read motion pic (on/off).
  - Read number of pics.
  - Read time between pics.
  - Read motion video (on/off).
  - Read quiet period.
  - Read Sensitivity.
  - Confirm it is Rapidfire.
  - Confirm it is 24 hours.
  - Navigate to Change Setup and USERLABEL (might not be necessary on the camera anymore because of the mass rename script).
  - Read current user label.
  - Change user label to CAMERAPOINTYEAR-TRIP (e.g., 02B2023-1).
  - Read new user label.
- Data Recorder:
  - Fill out datasheet with information read by camera trap handler.
  - While recording data, confirm prefilled metadata on the sheet matches what is being read.
  - If it does not match, edit the sheet manually with new changes.

### Mugshot Procedure:
- Take a mugshot upon arriving and leaving each camera trap site; additionally, perform the walk test before the final mugshot.
- To do a mugshot, write down the team name (i.e., UCSB2023), the date, and the time on a sheet of paper and make sure it's visible to the camera.
- If the camera light blinks when you approach, the batteries have not died yet, and it will take the mugshot.
- After you have taken the mugshot, open the camera and check if the batteries are on.
- If there was no light when you approached and there is NO text on the screen, the batteries are dead and need to be replaced at that moment.
- After you’ve replaced the batteries, when the camera turns on, record the date and time and any other information displayed on the screen. If the time is incorrect, change it at the end.
- Proceed to dictate the rest of the data to the data recorder role.
- If there IS text on the screen, the batteries still have some juice, and you can proceed to dictate the data to the data recorder role.
- Regardless of how much charge the batteries have, you will replace them once you’ve finished noting down the data.
- Then see how many pictures the camera took: check status.
- Record the settings the camera is on: change them to the correct settings if needed.
- Check the battery status: make sure to set on the lithium battery.
- Replace the batteries if they are not brand new.
- Do a walk test to see the camera span if needed.
- Arm the camera.
- Do another mugshot.

# Mass Rename and Model Instructions <a name="massandmodel"></a>
