#chmod +x <path to rpi_execution_code.py>
#sudo OPENBLAS_CORETYPE=ARMV8 pip install progressbar2

#pip3 install --extra-index-url https://google-coral.github.io/py-repo tflite_runtime

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

from tflite_runtime.interpreter import Interpreter #sudo OPENBLAS_CORETYPE=ARMV8 python3 -m pip install tflite-runtime
from PIL import Image
import numpy as np
import time
import os
import pandas as pd #sudo OPENBLAS_CORETYPE=ARMV8 pip3 install pandas
import datetime

import glob, os
from shutil import copyfile

fileName = input("Please enter the name of the file produced by mass_rename.sh, it should look something like 'metaData_....csv'\n")
#fileName = "year_camLoc_camID_tripNum.csv"
fileName = fileName.split("_",1)[1]

def load_labels(path): # Read the labels from the text file as a Python list.
   with open(path, 'r') as f:
    return [line.strip() for i, line in enumerate(f.readlines())]

def set_input_tensor(interpreter, image):
  tensor_index = interpreter.get_input_details()[0]['index']
  input_tensor = interpreter.tensor(tensor_index)()[0]
  input_tensor[:, :] = image

def classify_image(interpreter, image, top_k=1):
  set_input_tensor(interpreter, image)

  interpreter.invoke()
  output_details = interpreter.get_output_details()[0]
  output = np.squeeze(interpreter.get_tensor(output_details['index']))

  scale, zero_point = output_details['quantization']
  output = scale * (output - zero_point)

  ordered = np.argpartition(-output, 1)
  return [(i, output[i]) for i in ordered[:top_k]][0]

#print("Input model and labels parent directory: ")
#parent_directory = input()

#print("Input model name: ")
#model_name = input()

#print("Input class .txt file name: ")
#class_name = input()


#data_folder = parent_directory

# The following code will look within the folder titled "SCI_skunks" for the tflite_model folder and the model and label files

home_directory = os.path.expanduser("~")

# Search for SCI_skunks directory recursively
sci_skunks_path = None
for root, dirs, files in os.walk(home_directory):
    if "SCI_skunks" in dirs:
        sci_skunks_path = os.path.join(root, "SCI_skunks")
        break

if sci_skunks_path is None:
    raise FileNotFoundError("SCI_skunks directory not found in the home directory. Confirm the folder name cloned from github is SCI_skunks. If not, change it to SCI_skunks in the file manager.")

model_path = os.path.join(sci_skunks_path, "tflite_model/model-4.tflite")
label_path = os.path.join(sci_skunks_path, "tflite_model/class_labels.txt")

interpreter = Interpreter(model_path)
#print("Model Loaded Successfully.")

interpreter.allocate_tensors()

_, height, width, _ = interpreter.get_input_details()[0]['shape']


dict = {'imageLabel':[],
        'imageName':[],
        'accuracy':[],
        'classificationTimeStamp' : []}
results = pd.DataFrame(dict)

# Get the current username
username = os.getlogin()

# Use string concat to create the base_path  
base_path = "/media/" + username + "/"

sd_card_name = input("Please enter the name of the SD card (i.e. SDHC) : ")
  
sd_card_path = os.path.join(base_path, sd_card_name)

# Check if DCIM directory exists within the SD card path
dcim_path = os.path.join(sd_card_path, "DCIM")
if os.path.exists(dcim_path) and os.path.isdir(dcim_path):
    for (dirpath, dirnames, filenames) in os.walk(dcim_path):
        pass
else:
    raise FileNotFoundError("DCIM directory not found in the specified SD card. Check to make sure the DCIM folder in the SD card is called DCIM, if not change it to DCIM in the file manager. ")  

for (dirpath, dirnames, filenames) in os.walk(dcim_path):
    for filename in filenames:
        if filename.endswith('.jpg') or filename.endswith('.JPG'):  
          images = (os.sep.join([dirpath, filename]))
          timeOfClass = datetime.datetime.now() 

          # Load an image to be classified.
          image = Image.open(images).convert('RGB')
          #print("Original image size:", image.size)

          image = image.resize((width, height))
          #print("New image size:", image.size, end="\n\n")

          # Classify the image.
          label_id, prob = classify_image(interpreter, image)

          # Read class labels.
          with open(label_path, 'r') as f:
            labels = [line.strip() for i, line in enumerate(f.readlines())]

          # Return the classification label of the image.
          classification_label = labels[label_id]
          #print("Image Label:", classification_label,  " ", "\nImage Name:", images,  "\nAccuracy   :", np.round(prob*100, 2), "%.")



          current_entry = {'imageLabel': classification_label, "imageName": filename, 'accuracy': (np.round(prob*100, 2), "%."), "classificationTimeStamp" : timeOfClass}

          results = results._append(current_entry, ignore_index = True)
          
          print("classified image " + images)
              
csvName = "modelResults_" + str(fileName)

results.to_csv(csvName, sep=',', index=False)

#results.to_csv(csvName, sep=',', index=False)

print("Model results file for this camera has been created and saved in the current working directory under'" + csvName + "'")


