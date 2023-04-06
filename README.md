<p align="center">
    <strong>Santa Cruz Island Spotted Skunk Project</strong>
</p>

At the Smithsonian Office of Chief Information Officer (OCIO) Lab researchers use big data techniques, such as deep machine learning, to generate insights from their data, whether they are derived from genome sequencing, ecological sensors, or mass digitization of museum objects. These techniques require computational expertise in hardware and software to both build new algorithms and to implement the emerging tools on current and on-going project.

As mentioned new tools and algorithms are required to build process and harness and the data that is being collected and in this repository you will find a project repository tailored specifically towards an ongoing project done by the OCIO Lab at the California Channel Islands. 

# Table of Contents
- [1. Purpose](#Purpose)
- [2. Folders](#Folders)
  * [2.1 Shell_Scripts](#Shell_scripts)
    * [2.1.1 train_move.sh](#train_move.sh)
    * [2.1.2 mass_rename.sh](#mass_rename.sh)
  * [2.2 cameratrap-dp](#cameratrap-dp)
  * [2.3 markdown_images](#markdown_images)
  * [2.4 python_notebooks](#python_notebooks)
    * [2.4.1 ML_model.ipynb](#ML_model.ipynb)
    * [2.4.2 Renaming_moving.ipynb](#Renaming_moving.ipynb)
    * [2.4.3 deployMediaObs.py](#deployMediaObs.py)
    * [2.4.4 jsonToCsv.ipynb](#jsonToCsv.ipynb)
    * [2.4.5 jsonToCsv.py](#jsonToCsv.py)
    * [2.4.6 rpiClassify.py](#rpiClassify.py)
  * [2.5 tech_documents](#tech_documents)
  * [2.6 tflite_model](#tflite_model)
  * [2.7 txt_csv_direcotries](#txt_csv_direcotries)
- [3. Third Example](#third-example)
- [4. Fourth Example](#fourth-examplehttpwwwfourthexamplecom)


## Purpose

The purpose of this README.md file is to help you understand the purpose of the project as well as understanding the content and purpose of each folder in this repository. 

This document also serves as a procedural guide for various processes, detailing explicitly how to navigate the current model and data collection system so future interns and users of this software can understand and navigate it with ease. This software and document is written for students and mentors of the UCSB-Smithsonian Scholars Program as well as the OCIO Data science Lab.


## Folders
In this repository we see seven different folder, these folders all serve a different purpose and store different data files. This section will give you an end to end explanation of the type of files, data, and purpose file within the folders. 

### Shell_scripts
Within this folder you can find the following files:

  * [train_move.sh](https://github.com/sidatasciencelab/SCI_skunks/blob/main/Shell_scripts/trainMove.sh)
  * [mass_rename.sh](https://github.com/sidatasciencelab/SCI_skunks/blob/main/Shell_scripts/mass_rename.sh)
  

#### train_move.sh

The purpose of this file is to reorganize the files from a randomized data structure to a structure follwoing to the flowers data set (seen below). 
  <p align="center">
    <img src="markdown_image/beforeAfter.jpg" alt="Reorganized  Data Structure" width="500">
  </p>
  
  There are seven categories/folders that are going to be created from this script and will labeled as follows:
  
    1. Bird
    2. Empty
    3. Fox
    4. Human
    5. Other
    6. Rodent
    7. Skunkd
    
These files will then be refrenced by the [mass_rename.sh](https://github.com/sidatasciencelab/SCI_skunks/blob/main/Shell_scripts/mass_rename.sh) shell script so it is important to insure that names are correctly spelled and exactly as shown above.
  
#### mass_rename.sh
    
The purpose of this file is to rename the files with a unique name following a general schema. The renamed image will look similar to what is shown below and the purpose is to be able to more easily manage the data as well as store metadata within the name of the image to more easily understand where and when the image was taken.
  
  > **Sample Image Name:**  2022_02_2A_01_img_00001.jpg
  
  As you can see above we can easily tell that this picture takes on the follwing format!
  
  > **Sample Image Schema:**  Year_CameraLocation_CameraIdentificationNumber_TripNumber_img_00001.jpg
    
### cameratrap-dp: 

The content of this folder is to store sample files produced by [deployMediaObs.ipynb](https://github.com/sidatasciencelab/SCI_skunks/blob/main/python_notebooks/deploymediaobs.py). If there is any confusiion understnading the files please reference the techincal document [CamTrapDP.pdf](https://github.com/sidatasciencelab/SCI_skunks/blob/main/tech_documents/CamTrapDP.pdf), this file contains very in depth explanation of all the files found in this folder.

### markdown_images

The content of this folder is used to store images and other files referenced throughout the repository. None of these images/files in this folder are of significant importance with the exception of the README.md file. 

### python_notebooks

Within this folder you can find the following files/python notebooks:

  * [ML_model.ipynb](https://github.com/sidatasciencelab/SCI_skunks/blob/main/python_notebooks/ML_model.ipynb)
  * [Renaming_moving.ipynb](https://github.com/sidatasciencelab/SCI_skunks/blob/main/python_notebooks/Renaming_moving.ipynb)
  * [deployMediaObs.py](https://github.com/sidatasciencelab/SCI_skunks/blob/main/python_notebooks/deploymediaobs.py)
  * [jsonToCsv.ipynb](https://github.com/sidatasciencelab/SCI_skunks/blob/main/python_notebooks/jsonToCsv.ipynb)
  * [jsonToCsv.py](https://github.com/sidatasciencelab/SCI_skunks/blob/main/python_notebooks/jsonToCsv.ipynb)
  * [rpiClassify.py](https://github.com/sidatasciencelab/SCI_skunks/blob/main/python_notebooks/rpiClassify.py)

#### ML_model.ipynb 

This Python notebook contains the the source code to train our image classifying model. This model utilizes the Tensor Flow Lite Model Maker to train a model that is less GPU and storage intensive. The reason why we need to create such a model is becasue the Raspberry Pi's we are using are much smaller in terms of storage and and GPU capabilities. 

The steps this note book take to train the model are as follows 
  
    1. Installing Tensor Flow Lite
    2. Importing Required Libraries
    3. Importing Google Drive files
    4. Setting Image Path
    5. File Cleaning and Preparation
    6. Creating Train and Test Data From Images in image_path Directory
    7. Creating Validation and Test data From rest_data
    8. Tensor Flow Lite Model

Although we only see an overview of the steps the notebook performs we can, you can refrence the techincal document, [rpiClassify.py](https://github.com/sidatasciencelab/SCI_skunks/blob/main/tech_documents/Tensorflow_Lite_on_RPI_end_to_end-2.pdf) for an in depth explnation of the algorithm and steps used in this creation of the image classifying model. 

#### Renaming_moving.ipynb

This python notebook converts the the Annotation file affiliated with the dataset, found [here](https://lilablobssc.blob.core.windows.net/channel-islands-camera-traps/channel-islands-camera-traps.json.zip), from a Json data structure to a CSV data structure. 

We need to convert the file from a Json to CSV in order to work with it using various other notebooks and shell scripts.

#### deployMediaObs.py

It is important to structure the data in a method that is of common practice and easy to understand for researchers who use our data. For that reason we created the [deployMediaObs.py](https://github.com/sidatasciencelab/SCI_skunks/blob/main/python_notebooks/deploymediaobs.py) python executable file.

This Python Executable contains the the source code to convert files produced by [ML_model.ipynb](https://github.com/sidatasciencelab/SCI_skunks/blob/main/python_notebooks/ML_model.ipynb) into the [Camera Trap Data Package](https://tdwg.github.io/camtrap-dp/) format. As mention we must follow standard practice to share our findings and this python does that. 

It is important to understand what the the files produced signify and how they functino together. In order to understand the files, please reference the Technical Document, [CamTrapDP.pdf](https://github.com/sidatasciencelab/SCI_skunks/blob/main/tech_documents/CamTrapDP.pdf)n for an in depth explanation of what each PDF files contains and where they will be stored within the RPI.

### tech_documents
Throughout the construction of this project, we have put together a series of technical documents outlining the projects workflow and other aspects of the project. 

Within this folder you find the following files:

  * [CamTrapDP.pdf](https://github.com/sidatasciencelab/SCI_skunks/blob/main/tech_documents/CamTrapDP.pdf)
  * [Tensorflow_Lite_on_RPI_end_to_end-2.pdf](https://github.com/sidatasciencelab/SCI_skunks/blob/main/tech_documents/Tensorflow_Lite_on_RPI_end_to_end-2.pdf)
  * [Workflow___SCI_Skunks-2.pdf](https://github.com/sidatasciencelab/SCI_skunks/blob/main/tech_documents/Workflow___SCI_Skunks-2.pdf)
  * [jsonToCsv-5.pdf](https://github.com/sidatasciencelab/SCI_skunks/blob/main/tech_documents/jsonToCsv-5.pdf)
  * [mass_rename.pdf](https://github.com/sidatasciencelab/SCI_skunks/blob/main/tech_documents/mass_rename.pdf)
  * [trainMove-3.pdf](https://github.com/sidatasciencelab/SCI_skunks/blob/main/tech_documents/trainMove-3.pdf)
  
All of the files in this folder will be .pdf files and will be outlines and summaries of the Python notebooks, Shell Scripts, and all other execuatbale files that are found on within the [python_notebooks](https://github.com/sidatasciencelab/SCI_skunks/tree/main/python_notebooks), [Shell_scripts](https://github.com/sidatasciencelab/SCI_skunks/tree/main/Shell_scripts), and other folder containing exeecuatables. 

It is highly reccomended that you read through these files as it will help you understand content in other folders.

### tflite_model

### txt_csv_direcotries


## Third Example
## [Fourth Example](http://www.fourthexample.com)


2. Project Description
This is an important component of your project that many new developers often overlook.

Your description is an extremely important aspect of your project. A well-crafted description allows you to show off your work to other developers as well as potential employers.

The quality of a README description often differentiates a good project from a bad project. A good one takes advantage of the opportunity to explain and showcase:

What your application does,
Why you used the technologies you used,
Some of the challenges you faced and features you hope to implement in the future.


3. Table of Contents (Optional)
If your README is very long, you might want to add a table of contents to make it easy for users to navigate to different sections easily. It will make it easier for readers to move around the project with ease.


4. How to Install and Run the Project
If you are working on a project that a user needs to install or run locally in a machine like a "POS", you should include the steps required to install your project and also the required dependencies if any.

Provide a step-by-step description of how to get the development environment set and running.

5. How to Use the Project
Provide instructions and examples so users/contributors can use the project. This will make it easy for them in case they encounter a problem – they will always have a place to reference what is expected.

You can also make use of visual aids by including materials like screenshots to show examples of the running project and also the structure and design principles used in your project.

Also if your project will require authentication like passwords or usernames, this is a good section to include the credentials.

<p align="center">
    <strong>Santa Cruz Island Spotted Skunk Project</strong>
</p>

 A ML workflow for identifying spotted skunks from camera trap images taken on Santa Cruz Island in California's Channel Islands
<p align="center">
    <img src="markdown_image/santa_cruz_island.jpeg" alt="santa cruz island" width="500">
</p>

## Background
On the Channel Islands there are many species of animals, some that are endemic and other that are not. One example of the an endemic species would be the island spotted skunk (Spilogale gracilis amphialus) is an insular endemic carnivore and a subspecies of the western spotted skunk (Spilogale gracilis). The skunk is only currently found on two islands off the southern coast of California (Santa Cruz Island, and Santa Rosa Island, where its occurrence is rare). Its presence has been recorded on San Miguel Island, but it has since been declared extinct in that area. The Channel Island skunk is one of two terrestrial carnivores on the islands, the other being the island fox. It is designated as a species of special concern by the state of California as its population has seen a regression in the recent years. For this reason the National Park Service, Smithsonian OCIO Data Science lab as well as the Smithsonain Scholars Program at UCSB have taken on the on going project of using machine learning & artificiall intelligence to help analyze the popluation and decide weather this species of special concern should be declared endangered or not. 

## Methods

As previously mentioned, since mid 2018 the National Park Service (NPS), Smithsonian Offie of Chief Information Officer (OCIO) Data Science Lab, and the UC, Santa Barbara Office Smithsonian Scholars have partnered together to analyze the spotted skunk poplution. On the Santa Rosa Island, we are using the Date/Time stamps on a number remote cameras which have been operating continuously from October 2018 to present to assess seasonal activity patterns of island spotted skunk and island fox. These cameras are motion activiated and are sensative to the motion of a motving branch, passing skunk or flying bird, ultamitly causing them to take thousands of pictures a day most of which are empty pictures. We however don't know which are empty and which are not so we must anylyze them one by taking up a lot of time and resources. For this reason we have decided to employ machine learning as to automate our workflow 

<p align="center">
    <img src="markdown_image/reconyx_hyperfire_camera.jpeg" alt="reconyx hyperfire camera" width="500">
</p>

### Data Mining Relavent Data

Since we have partner with the NPS and the Smithonian OCIO Data Science lab we have access to more than 240,000 annoted images located on the [
Labeled Information Library of Alexandria: Biology and Conservation (LILA BC)](https://lila.science/datasets/channel-islands-camera-traps/) which follow the [COCO Data Set format](https://www.section.io/engineering-education/understanding-coco-dataset/) as well acess to 2,500 annoted images annoted using stadard practice.  


### Tidy Data 

#### Renaming and Normalizing Data

As mentioned, images from the LILA BC data set were annoted using the COCO dataset format and were normalized using best practices which can be found in the ```python_notebooks/renaming_moving.ipynb``` file as well as the ```shell_scripts/mass_move.sh```. In addition to this, we collected camera trap data. given that we are processing images from from over X_NUM cameras we are therefor receiving thousands of images everytime we go into the field. For this reason we must be  able to keep track of the images site number, camera number, expedition number, and other metadata that we must include as part of our preprocessing procedure. To do this in an fast effecient manner we created a shell script that takes in n vairables and renames the images with those n variables which the user designates. 

```
shell_scripts/mass_rename.sh
```

Once the rename naming was finsihed, I was left to reorganize the dataset into a format which [```tflite_model_maker.image_classifier.DataLoader.from_folder()```](https://www.tensorflow.org/lite/api_docs/python/tflite_model_maker/image_classifier/DataLoader) could read. I structured my data in a similiar way to to that of the [Flowers Data Set](https://www.kaggle.com/datasets/alxmamaev/flowers-recognition). 
```
└── Desktop
   └── Parents_directory 
           └── Class_1 
           |     ├── Class_1_img_1.jpg
           |     ├── Class_1_img_4.jpg
           |     ├── Class_1_img_2.jpg
           |     └── Class_1_img_3.jpg  
           └── Class_2 
           |     ├── Class_2_img_1.jpg
           |     ├── Class_2_img_4.jpg
           |     ├── Class_2_img_2.jpg
           |     └── Class_2_img_3.jpg  
           └── Class_3 
           |     ├── Class_3_img_1.jpg
           |     ├── Class_3_img_4.jpg
           |     ├── Class_3_img_2.jpg
           |     └── Class_3_img_3.jpg  
           └── Class_4 
                 ├── Class_4_img_1.jpg
                 ├── Class_4_img_4.jpg
                 ├── Class_4_img_2.jpg
                 └── Class_4_img_3.jpg  
```

### Model Architecture 

Since we will be running this model on edge devices, specifically the [Raspberry Pi 400](https://www.raspberrypi.com/products/raspberry-pi-400/), I choose to use the TensorFlow Lite [efficientnet_lite3 for image classification](https://tfhub.dev/tensorflow/efficientnet/lite3/classification/2) as it doesn't require as strong of a GPU as other conventional methods such as the ResNet50, YoloV5, etc. 
 
