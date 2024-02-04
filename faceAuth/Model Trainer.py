import cv2
import numpy as np
from PIL import Image
import os

# Path for samples already taken
path = 'Face-Recognition-main/samples'

# Create LBPH recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Load Haar Cascade classifier for face detection
detector = cv2.CascadeClassifier("Face-Recognition-main/haarcascade_frontalface_default.xml")

def Images_And_Labels(path):
    # Fetch the images and labels
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]     
    faceSamples = []
    ids = []

    for imagePath in imagePaths:
        # Convert image to grayscale
        gray_img = Image.open(imagePath).convert('L')
        img_arr = np.array(gray_img, 'uint8')

        # Extract ID from the filename
        id = int(os.path.split(imagePath)[-1].split(".")[1])

        # Detect faces in the image
        faces = detector.detectMultiScale(img_arr)

        for (x, y, w, h) in faces:
            faceSamples.append(img_arr[y:y+h, x:x+w])
            ids.append(id)

    return faceSamples, ids

print("Training faces. It will take a few seconds. Please wait...")

# Train the recognizer with the images and corresponding IDs
faces, ids = Images_And_Labels(path)
recognizer.train(faces, np.array(ids))

# Save the trained model
trainer_path = 'Face-Recognition-main/trainer/trainer.yml'
recognizer.write(trainer_path)

print("Model trained. Now we can recognize your face.")
