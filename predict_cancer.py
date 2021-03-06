# import the necessary packages
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import matplotlib.pyplot as plt
from imutils import build_montages
from imutils import paths
import numpy as np
import argparse
import random
import cv2


def predict_image(imagePaths):
    # load the pre-trained network
    print("[INFO] loading pre-trained network...")
    model = load_model("cancer.model")

    results = []

    orig = cv2.imread(imagePaths)

    image = cv2.cvtColor(orig, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (48, 48))
    image = image.astype("float") / 255.0

    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)

    pred = model.predict(image)
    
    i = pred.argmax(axis=1)[0]

    print(f"[INFO] Predicted class {'Cancer' if i == 0 else 'NoCancer'}")
    
    label = "Cancer is detected" if i == 0 else "Cancer is not detected"
    color = (0, 0, 255) if i == 0 else (255, 0, 0)

    text = "{}: {:.2f}%".format(label, pred[0][i]*100)

    orig = cv2.resize(orig, (600, 600))
    cv2.putText(orig, text, (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 3)

    # add the output image to our list of resultss
    results.append(orig)

    print("[INFO] Showing the image")

    return orig

