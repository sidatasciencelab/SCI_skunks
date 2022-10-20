#pip3 install --extra-index-url https://google-coral.github.io/py-repo tflite_runtime

from tflite_runtime.interpreter import Interpreter 
from PIL import Image
import numpy as np
import time
import os

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

data_folder = "/home/pi/Downloads/SCI_skunk-main/"

model_path = data_folder + "model-4.tflite"
label_path = data_folder + "class_labels.txt"

interpreter = Interpreter(model_path)
#print("Model Loaded Successfully.")

interpreter.allocate_tensors()
_, height, width, _ = interpreter.get_input_details()[0]['shape']
print("Image Shape (", width, ",", height, ")")
dict = {'Image Label':[],
        'Image Name':[],
        'Accuracy':[]}
results = pd.DataFrame(dict)
for images in os.listdir("/content/test_images/"):
 
    # check if the image ends with png
    if (images.endswith(".JPG") or images.endswith(".jpg")):
    # Load an image to be classified.
        image = Image.open(data_folder + images).convert('RGB').resize((width, height))

        # Classify the image.
        time1 = time.time()
        label_id, prob = classify_image(interpreter, image)
        time2 = time.time()
        classification_time = np.round(time2-time1, 3)
        #print("Classificaiton Time =", classification_time, "seconds.")

        # Read class labels.
        labels = load_labels(label_path)

        # Return the classification label of the image.
        classification_label = labels[label_id]
        #print("Image Label is :", classification_label, ", with Accuracy :", np.round(prob*100, 2), "%.")
        current_entry = {'Image Label': classification_label, "Image Name": images, 'Accuracy': (np.round(prob*100, 2), "%.")}

        results = results.append(current_entry, ignore_index = True)
        
results.head()

