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

## 1. Approaching the Camera Trap
1. **Take a Mugshot**:
   - Write the Camera #: UCSBCameraID (e.g., "UCSB02") and the date on the SCI Spotted Skunk folder’s laminated mugshot paper using a dry erase marker.
   - Approach the camera trap with the mugshot paper visible to it and within its range.
   - If the camera light blinks, the batteries are still functioning and the camera will take the mugshot.

## 2. Replacing Batteries and Collecting Metadata
1. **Assign Roles**:
   - **Data Recorder**: Tracks the metadata on the sheet.
   - **Camera Trap Handler**: Reads metadata to the data recorder.

2. **Camera Trap Handler Tasks**:
   - **Check and Replace Batteries**:
     - Open the camera and check the battery charge status.
     - Replace batteries and store old ones in the used batteries Ziploc bag.
     - Check the charge status of the new batteries.
   - **Record Metadata**:
     - Navigate to and read the following settings:
       - **Battery Type**
       - **Status/About**:
         - Number of images on the card
         - Time (adjust if incorrect)
         - Date
         - Version number
         - Serial number
       - **Change Setup**:
         - **Motion**:
           - Motion pic (on/off)
           - Number of pics
           - Time between pics
           - Motion video (on/off)
           - Quiet period
           - Sensitivity
         - Confirm it is set to Rapidfire
         - Confirm it is set to 24 hours
       - **User Label** (if needed):
         - Read current user label
         - Change user label to CAMERAPOINTYEAR-TRIP (e.g., "02B2023-1")
         - Read new user label

3. **Data Recorder Tasks**:
   - Fill out the datasheet with the information read by the camera trap handler.
   - Confirm that prefilled metadata on the sheet matches the data being read.
   - Edit the sheet manually if there are any discrepancies.
   - Have someone else double-check the recorded data and fill out the “Data Sheet Reviewer” section.

## 3. Departing from the Camera Trap
1. **Final Steps**:
   - If necessary, perform a walk test to check the camera range.
   - Arm the camera.
   - Take another mugshot by approaching the camera with the mugshot paper. The camera will blink if it detects you.

# Mass Rename and Model Instructions <a name="massandmodel"></a>
