
for direc in ~/Desktop/Image_address/bird_list.txt ~/Desktop/Image_address/empty_list.txt ~/Desktop/Image_address/fox_list.txt ~/Desktop/Desktop/Image_address/skunk_list.txt #iterating through .txt files which contain directories for each class
do
    for folder in ~/Desktop/training_images/bird ~/Desktop/training_images/empty ~/Desktop/training_images/fox ~/Desktop/training_images/ skunk #iterating through folders that I want respective files to be placed in. 
    do
        for file in $(cat $direc);  #reading in each directory 
        do
            echo mv "$file" $folder; #moving file to corresponding directory
        done
    done
done

