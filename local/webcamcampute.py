import cv2
import os
import time
import uuid
import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.models import Model
from sklearn.neighbors import NearestNeighbors
import sys

project_path = "C:\\Users\\canud\\OneDrive\\Desktop\\project\\Amanage"  # Replace with the correct path to your project folder
sys.path.append(project_path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE","Amanage.settings")
import django
django.setup()
from local.models import entrydetails


# Function to save images to a directory with labels and generate a random UUID
def save_images_with_uuid(directory, num_images, label):
    # Create the directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # Generate a random UUID for this run
    run_id = str(uuid.uuid4())[:8]
    
    # Open the webcam
    cap = cv2.VideoCapture(0)
    
    count = 0 
    while count < num_images:
        # Capture frame from the webcam
        ret, frame = cap.read()
        
        # Display the captured frame
        cv2.imshow('Capture Images', frame)
        
        # Save the frame as an image file with label and run ID
        image_path = os.path.join(directory, 'image{}_{}_{}.jpg'.format(count, label, run_id))
        cv2.imwrite(image_path, frame)
        
        count += 1
        
        time.sleep(0.5)

        # Exit the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release the webcam and close the OpenCV window
    cap.release()
    cv2.destroyAllWindows()

    # Return the generated UUID
    return run_id

#Save images from webcam with labels and get the random UUID
# label = input("Enter the label for the captured images: ")
# uuid = save_images_with_uuid('image_data', 10, label)
# print("Random UUID:", uuid)

folder_path = 'image_data'


for filename in os.listdir('image_data'):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        image_path = os.path.join(folder_path,filename)
        img = cv2.imread(image_path)


        cv2.waitKey(0)

cv2.destroyAllWindows()

def extract_features(directory, model):
    features = {}
    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        image = load_img(path, target_size=(224, 224))
        image = img_to_array(image)
        image = np.expand_dims(image, axis=0)
        image = preprocess_input(image)
        feature = model.predict(image).flatten()
        features[filename] = feature
    return features

# Path to the dataset directory
dataset_directory = 'image_data'

# Load pre-trained VGG16 model without the top (fully connected) layer
base_model = VGG16(weights="imagenet", include_top=False)
model = Model(inputs=base_model.input, outputs=base_model.output)

# Extract features from dataset images
dataset_features = extract_features(dataset_directory, model)

# print(dataset_features)
# print(dataset_features.__sizeof__())
# print(dataset_features.typ)

feature = entrydetails()
feature.original_features = dataset_directory

#feature.save()
print('NASU')
print(entrydetails.original_features,entrydetails.name_student)
sys.exit(dataset_features)