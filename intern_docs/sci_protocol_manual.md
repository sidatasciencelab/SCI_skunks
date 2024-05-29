---
title: "SCI Protocol Skunk Crew Manual"
author: "Richard Montes Lemus"
date: "May 28, 2024"
---
# Introduction
The Island Spotted Skunk Monitoring Project is a collaboration between the Smithsonian Data Science Lab and the UCSB Office of Education Partnerships. This manual outlines the steps Skunk Crew members should follow to ensure an efficient workflow, from the pre-trip preparations to final data submission.

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
- Follow detailed steps for collecting data at camera trap sites, replacing batteries, and documenting field notes and metadata on data sheets. See [Updated Camera Trap Data Collection Protocol](#protocol). 

## Data Processing
- Ensure your Rasberry Pi is set up correctly, and all scripts run correctly. See [Re-Installing Raspberry Pi Software and Setting Up the SCI_skunks Environment](#rpi_github).
- Process collected SD cards using the mass rename script, the machine learning model script, and the deploy media observation script. See [Mass Rename and Model Instructions](#massandmodel). 
- Generate CSV files from all three scripts and compile relevant field notes and metadata from the data sheets for each camera trap site - they will be used in Post-Trip Procedures: Data Management.
### Inventory Update
- Update inventory lists based on field requirements before leaving the island.

## Post-Trip Procedures
### Return to UCSB
- Transportation of equipment, food, and secure data back to UCSB.
### Data Management
- Store metadata sheets and data safely.
- Compilation and organization of CSV files using concatenated_sci_csv.py script. See [Camtrap DP CSV File Concatenation](#concatenate).
### Data Submission
- Take concatenated scripts and camera trap images for every trip and store them on a hard drive
- Take concatenated scripts and camera trap images for every trip on the hard drive and send them to the       
  Smithsonian's Hydra computer using Globus.
- Upload metadata sheets and deploy media observation CSV files to GitHub.
- Take a picture of metadata sheets and upload it to GitHub.
- Store metadata datasheets and hard drives somewhere safe.

# Conclusion
Completing these steps ensures the efficient collection, processing, and submission of data for the Island Spotted Skunk Monitoring Project.


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
   - Write the Camera #: UCSBCameraID (e.g., "UCSB02") and the date on the SCI Spotted Skunk folder’s laminated mugshot paper using a dry-erase marker.
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
         - Read the current user label
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

# Re-Installing Raspberry Pi Software and Setting Up the SCI_skunks Environment <a name="rpi_github"></a>  
## Reinstalling the Raspberry Pi Software
1. **Download and Install Raspberry Pi Imager**:
   - [Download Raspberry Pi Imager Software](https://www.raspberrypi.com/software/)
2. **Prepare the SD Card**:
   - Obtain the SD card from the Raspberry Pi and insert it into your computer.
3. **Open Raspberry Pi Imager**:
   - Launch the Raspberry Pi Imager on your computer.
4. **Reset and Install Software**:
   - Follow the on-screen instructions in the Raspberry Pi Imager to reset the software and install the latest version.

## Downloading the SCI_skunks Folder from GitHub and Changing Permissions

### Cloning the Repository
1. **Change to the Downloads Directory**:
   ```bash
   cd ~/Downloads
   ```
2. **Clone the SCI_skunks Repository**:
   ```bash
   git clone https://github.com/sidatasciencelab/SCI_skunks.git
   ```
### Changing Permissions
1. **Change to the SCI_skunks Directory**:
   ```bash
   cd ~/Downloads/SCI_skunks
   ```
2. **Make Scripts Executable**:
   - For rpiClassify.py
   ```bash
   chmod u+x python_notebooks/rpiClassify.py
   ```
   - For deployMediaObs.py
   ```bash
   chmod u+x python_notebooks/deployMediaObs.py
   ```
   - For mass_rename.sh
   ```bash
   chmod u+x Shell_scripts/mass_rename.sh
   ```

## Downloading Miniforge and Creating the skunkEnv Environment
### Installing Miniforge
1. **Download Miniforge Installer**:
   ```bash
   wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-aarch64.sh
   ```
2. **Run the Miniforge Installer**:
   ```bash
   Miniforge3-Linux-aarch64.sh
   ```
3. **Follow the Installation Instructions**:
   If prompted, update Miniforge and follow the on-screen instructions.

## Setting Up skunkEnv Environment
1. **Download spec-file.txt**:
   - Ensure spec-file.txt is placed in the Downloads folder on your Raspberry Pi.
2. **Open a New Terminal**:
3. **Change to the Downloads Directory**:
   ```bash
   cd ~/Downloads
   ```
4. **Create the skunkEnv Environment**:
   ```bash
   conda create --name skunkEnv
   ```
5. **Activate the skunkEnv Environment**:
   ```bash
   conda activate skunkEnv
   ```
6. **Install Dependencies from spec-file.txt**:  
   ```bash
   conda install --name skunkEnv --file spec-file.txt
   ```
    - If you encounter issues with the above steps, you can create the environment directly using:
   ```bash
   conda create --name skunkEnv --file spec-file.txt
   ```
## Activating skunkEnv Environment
Activate the Environment:
bash
Copy code
conda activate skunkEnv
Saving the Spec File for Future Use
Generate the Spec File:
To get the spec file from any Raspberry Pi in the future, run:
bash
Copy code
conda list --explicit > spec-file.txt

# Mass Rename and Model Instructions <a name="massandmodel"></a>
## 1. Insert SD Card
1. **Insert SD Card**:
- Insert the SD card into the adapter in the back of the Raspberry Pi.

## 2. Open File Explorer
1. **Access SD Card**:
- Click on the “File Explorer” folder icon at the top left of the screen.
- Once the window is open, click the name of the SD card (e.g., `SDCARD`) at the top left of the window.
- Confirm that your images on the SD card appear.

## 3. Rename the SD Card
1. **Rename SD Card**:
- Rename the SD card to a name without spaces (e.g., `SDCARD`).
- To rename it, right-click the folder with its name and select rename.

## 4. Open Terminal and Set Working Directory
1. **Open Terminal**:
- Open a terminal window with `ctrl + alt + t`.
2. **Set Directory**:
- Set your working directory to your SD card folder by entering the command:
     ```bash
     cd /media/zachary/SDCARD/DCIM
     ```

## 5. Run the mass_rename.sh Script
1. **Execute Script**:
- Enter the following command in the terminal:
     ```bash
     /home/zachary/Downloads/SCI_skunks/Shell_scripts/mass_rename.sh
     ```
2. **Provide Inputs**:
- When prompted for the parent directory, enter:
     ```bash
     /media/zachary/SDCARD/DCIM
     ```
- When prompted for the `mass_rename.sh` file directory, enter:
     ```bash
     /home/zachary/Downloads/SCI_skunks/Shell_scripts
     ```
- When prompted for the file extension, enter the file extension provided by your camera (default is `JPG`).
- Choose `4` as the number of included variables.
- Name the variables in this order: `year`, `trip number`, `camera location`, `location ID`. Enter the corresponding values in the next prompt, capitalizing the letter in location ID for consistency and including zeros for single digits (e.g., `year = 2023`, `trip number = 01`, `camera location = 05`, `location ID = 5A`).
- Enter `y` when asked to run the function in debug mode.
- Confirm that debug mode gives the correct output.
- Enter `y` to run with previous entries.

## 6. Verify File Names and Metadata
1. **Check Files**:
- Go back to the SD card folder via the instructions in step 2.
- Note that the file names for all images have been changed according to the variable values entered.
- Note that there is a CSV file created called `metaData.csv`.

## 7. Activate skunkEnv Environment
1. **Activate Environment**:
- In the terminal, enter the command:
     ```bash
     conda activate skunkEnv
     ```

## 8. Run rpiClassify.py Script
1. **Execute Script**:
- In the terminal, enter the command:
     ```bash
     python3.9 /home/zachary/Downloads/SCI_skunks-main/python_notebooks/rpiClassify.py
     ```
2. **Provide Inputs**:
- Enter the name of the CSV file created by `mass_rename.sh` when prompted. The machine learning model will now begin classification.
- Enter the name of the SD card exactly as it appears in the file manager.
3. **Check Results**:
- Once finished, open the SD card folder and note a new CSV file titled `model_results.csv`.

# Camtrap DP CSV File Concatenation <a name="concatenate"></a>
