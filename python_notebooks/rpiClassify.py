#chmod +x <path to rpi_execution_code.py>
#sudo OPENBLAS_CORETYPE=ARMV8 pip install progressbar2

#pip3 install --extra-index-url https://google-coral.github.io/py-repo tflite_runtime

from tflite_runtime.interpreter import Interpreter #sudo OPENBLAS_CORETYPE=ARMV8 python3 -m pip install tflite-runtime
from PIL import Image
import numpy as np
import time
import os
import pandas as pd #sudo OPENBLAS_CORETYPE=ARMV8 pip3 install pandas
import datetime
import warnings

import glob
from shutil import copyfile

warnings.simplefilter(action='ignore', category=FutureWarning)

listing = glob.glob("/media/pi/*/DCIM1/envVars.csv") #using wild card to find the specific file names envVars.csv that is in the DCIM1 folder
for filename in listing:
  envVars = pd.read_csv(filename, sep = "=") #customo delimeter "=" rather than normal ',' 


fileName = envVars.loc[envVars.Variables=="fileNamesMeta"].Values #extracting csv file name that will be convension for the rest of the files created 



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

#model_path = data_folder+ "/" + model_name
#label_path = data_folder + "/" + class_name

model_path = "/home/pi/Downloads/SCI_skunks-main/tflite_model/model-4.tflite"
label_path = "/home/pi/Downloads/SCI_skunks-main/tflite_model/class_labels.txt"

interpreter = Interpreter(model_path)
#print("Model Loaded Successfully.")

interpreter.allocate_tensors()

_, height, width, _ = interpreter.get_input_details()[0]['shape']


dict = {'imageLabel':[],
        'imageName':[],
        'accuracy':[],
        'classificationTimeStamp' : []}
results = pd.DataFrame(dict)


for (dirpath, dirnames, filenames) in os.walk("/media/pi/C060-4E55/DCIM1"):
    for filename in filenames:
        if filename.endswith('.jpg'):  
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



          current_entry = {'observationType': classification_label, "imageName": fileName, 'classificationConfidence': (np.round(prob*100, 2), "%."), "classificationTimestamp" : timeOfClass}

          results = results.append(current_entry, ignore_index = True)
          
          print("classified image " + images)
              
csvName = "modelResults_" + str(fileName)

results.to_csv(csvName, sep=',', index=False)

#results.to_csv(csvName, sep=',', index=False)

print("Model results file for this camera has been created and saved in the current working directory under'" + csvName + "'")


