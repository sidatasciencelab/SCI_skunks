echo "WARNING: double check varaibles before executing script"
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
 
- The structure above shows the destination and source directories. All jpg files inside of the source directory's (Parent Direcotry) subdirectories (100RECNX) are copied into the destination folder with with the intended metadata and file name. 
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
Upon running the shell script you will be promt with intructions and various input types.
FOLLOW INSTRUCTIONS CLOSELY TO AVOID MSITAKES : )
    1. Locate the parent directory and do "cd parent directory"
	1) Go to your local storage/files where is the card is found. 
	2) Right click on parent directory with image. 
        * Should be called DCIM. 
	3) Click "Copy Path"
    4) Enter the path you just copied in the line that promts "Parent direcoty: "
	5) Next you will be asked "How many variables do you want to include in your file name: " you input should be numeric and only numeric.
    6) Next you will be asked to enter "Enter variable name". 
        * Variable names should be input int he order that you want them to be attatched to file name. 
    7) Next you will be asked to enter "Enter variable value name". 
        * For this part avoid spaces, any other inoput is acceptable.
    8) We advice running in debugging mode at least once so that you can check for typos or mistakes in your typing or destination path 
    
    
############################################################################################################################################################################################################################
​"
read -p 'Parent direcoty: ' read_location; #location of parent directory for images sd card location

i=0; for f in */*.JPG; do mv -- "$f" "parent_$((++i)).${f##*.}"; done  

#read -p 'What file format will you be ranaming? If you want to rename all files enter "*": ' file_type

#xport file_type
export read_location

vars=()
values=()

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
mkdir $regex

#read -p 'Destination directory: ' destination;
destination="${read_location}/${regex}/" #directory of where we want pictures to be coppied to
read -r -p "Would you like to run this function in debug mode? [y/N] " response
echo $destination
export destination
case "$response" in
    [yY][eE][sS]|[yY]) 
        find "${read_location}" -type f -iname '*.JPG' -exec sh -c '
        img_num="${1##*_}";  
        echo mv "${1}" "${destination}${regex}_${img_num}" 
        ' sh_cp {} \;
        read -r -p "If this looks correct, enter [y/N] to run with previous entries  " yesorno
        case "$yesorno" in
            [yY][eE][sS]|[yY])  
                find "${read_location}" -type f -iname '*.JPG' -exec sh -c '
                img_num="${1##*_}";
                mv "${1}" "${destination}${regex}_${img_num}"
                ' sh_cp {} \;
                ;;
            *)
                echo "Try again an be sure to check your variables twice "
                ~/*/*/mass_rename.sh
                ;;
            esac
        ;;
    *)
        find "${read_location}" -type f -iname '*.JPG' -exec sh -c '
        img_num="${1##*_}";
        mv "${1}" "${destination}${regex}_${img_num}"
        ' sh_cp {} \;
        ;;
esac


echo 
"

           *       ,MMM8&&&.            *
                  MMMM88&&&&&    .
                 MMMM88&&&&&&&
     *           MMM88&&&&&&&&
                 MMM88&&&&&&&&
                 'MMM88&&&&&&'
                   'MMM8&&&'      *    
          |\___/|     /\___/|
          )     (     )    ~( .               '
         =\     /=   =\~    /=
           )===(       ) ~ (
          /     \     /     |
          |     |     ) ~   (
         /       \   /     ~ |
         \       /   \~     ~/
  jgs_/\_/\__  _/_/\_/\__~__/_/\_/\_/\_/\_/\_
  |  |  |  |( (  |  |  | ))  |  |  |  |  |  |
  |  |  |  | ) ) |  |  |//|  |  |  |  |  |  |
  |  |  |  |(_(  |  |  (( |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |\)|  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

"