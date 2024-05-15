#sudo apt install exiftool


echo "WARNING: double check variables before executing script"
echo"
​############################################################################################################################################################################################################################
- This script renames every jpg file inside parent directory to include necessary metadata (camera name, zone, date, etc), and places them inside a single destination folder.
- The parent directory must follow the following structure:


├── Parent Directory
│   └── DCIM
│       └── reconyx
│           └── 100RECNX 
|                ├── img_1.jpg
|                ├── img_4.jpg
|                ├── img_2.jpg
|                └── img_3.jpg                
└── Destination_directory




​
- The structure above shows two folders. They are both located within the same directory, such as one's desktop folder. Destdir is the destination directory, which is the directory we want the renamed files to go. The srcdir is the source directory, which is the source of our files that we want to be renamed. When the shell scrip below is executed (with the intended metadata and destination folder entered), all jpg files will be renamed and copied into a single destination folder (ex. destdir). The structure below will outline how the .jpg files are renamed and copied into 
​
├── User
│   └── DCIM
│       └── reconyx
│           └── 100RECNX                 
├── Destination_directory
            ├── zone_trip_num_cam_num_img_1.jpg
            ├── zone_trip_num_cam_num_img_4.jpg
            ├── zone_trip_num_cam_num_img_2.jpg
            └── zone_trip_num_cam_num_img_3.jpg
 
- The structure above shows the destination and source directories. All jpg files inside of the source directory's (Parent Directory) subdirectories (100RECNX) are copied into the destination folder with with the intended metadata and file name. 
​
Shell script description (what the code means): 
​
This function is a great function to use when cleaning and tidying data as you might have multiple files that share the same name (i.e. img_1 in 100RECNX and img_1 in 101RECNX). 
If the user were to go around and collect the data from multiple sources the user could make them unique based based on the zone, cam_name, & trip_num. 


- 
- 
- 
- 
- 


{For Mac users}
To use this program on any MAC/MACBOOK you can do the following:
    1. Locate the parent directory and do "cd parent directory"
    2. Locate the parent directory and copy the folder path 
        * How to copy path name
            1. Open Finder
            2. Right click on folder name
            3. Under "General" tab you will find a section called "Where"
            4. Click on that file path and select "Copy as file path"
    3. Enter that in the "Parent directory: " section and name everything as you like.
    4. There is no need to create a destination directory as it is created for you as part and renamed images are automatically sent there
    5. We advice running in debugging mode at least once so that you can check for typos or mistakes in your typing or destination path
"


echo"
{For Raspberry Pi users}
Upon running the shell script you will be prompted with instructions and various input types.
FOLLOW INSTRUCTIONS CLOSELY TO AVOID MISTAKES : )
    1. Locate the parent directory and do "cd parent directory"
	1) Go to your local storage/files where is the card is found. 
	2) Right click on parent directory with image. 
        * Should be called DCIM. 
	3) Click "Copy Path"
    4) Enter the path you just copied in the line that prompts "Parent directory: "
	5) Next you will be asked "How many variables do you want to include in your file name: " your input should be numeric and only numeric.
    6) Next you will be asked to enter "Enter variable name". 
        * Variable names should be input in the order that you want them to be attatched to file name. 
    7) Next you will be asked to enter "Enter variable value name". 
        * For this part avoid spaces, any other input is acceptable.
    8) We advise running in debugging mode at least once so that you can check for typos or mistakes in your typing or destination path 
    
    
############################################################################################################################################################################################################################
​"
read -p 'Parent directory: ' read_location; #location of parent directory for images sd card location
read -p 'mass_rename.sh file directory: ' mass_rename_direct; #location of parent directory for images sd card location


#we will change this to the correct amount wildcards depending on RPI home directory 
#assuming that the SD card will mount in same location everytime without error.






#xport file_type
export read_location
export mass_rename_direct




vars=()
values=()


read -p 'Enter the file extension of the format you want to rename. Note that input is case sensitive (e.g, jpg, JPG, png, PNG): ' file_extension


read -p "How many variables do you want to include in your file name: " cvar
loop=1
while [ $loop -le $cvar ]
do
    read -p "Enter variable names #${loop}: " vars[$loop]
    loop=$((loop+1))
done
loop=1
while [ $loop -le $cvar ]
do
    read -p "Enter ${vars[loop]} value: " values[$loop]
    loop=$((loop+1))
done


echo "${values[*]}"
echo "${vars[*]}"


separator="_" 
foo=$values
regex="$( printf "${separator}%s" "${values[@]}" )"
regex="${regex:${#separator}}" 






export regex;
#mkdir $regex


#read -p 'Destination directory: ' destination;
#destination="${read_location}/${regex}/" #directory of where we want pictures to be coppied to
read -r -p "Would you like to run this function in debug mode? [y/N] " response
#echo "${destination}"
export destination


i=1


case "$response" in
    [yY][eE][sS]|[yY]) 
            a=0
            while [ $a -lt 15 ]
            do
                dir=("${read_location}"/*/*."${file_extension}")
                img_num="${dir[a]##*_}"
                printf '%q\n' "${destination}${regex}_${img_num}"
                a=`expr $a + 1`
            done
        read -r -p "If this looks correct, enter [y/N] to run with previous entries  " yesorno
        case "$yesorno" in
            [yY][eE][sS]|[yY])  
                for dir in "${read_location}"/*; do
                        [ -d "${dir}" ] || continue
                        for img in "${dir}"/*."${file_extension}"; do
                                [ -e "${img}" ] || break
                                new="$(printf "${regex}_img_%05d.${file_extension}" "${i}")"
                                mv "${img}" "$(dirname "${img}")/${new}"
                                ((i++))
                        done
                done
                ;;
            *)
                echo "Try again an be sure to check your variables twice "
                #/home/pi/Downloads/SCI_skunks-main/Shell_scripts/mass_rename.sh #change this to the where the local file will be stored on RPI 
                bash "${mass_rename_direct}"
                ;;
            esac
        ;;
    *)
        for dir in "${read_location}"/*; do
                [ -d "${dir}" ] || continue
                for img in "${dir}"/*.jpg; do
                        [ -e "${img}" ] || break
                        new="$(printf "${regex}_img_%05d.${file_extension}" "${i}")"
                        mv "${img}" "$(dirname "${img}")/${new}"
                        ((i++))
                done
        done
        ;;
esac
#img_num="${dir[a]##*_}"


echo "Now we are creating csv and saving it to the sd card" 


exiftool -csv */*."${file_extension}" > "metaData_${regex}_bin.csv" 
#using same metadata to create csv name
cat metaData_${regex}_bin.csv | tr -d '\0' > metaData_${regex}.csv








