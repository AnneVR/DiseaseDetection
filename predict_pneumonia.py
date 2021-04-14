# import the necessary packages
from keras.preprocessing.image import img_to_array
from keras.models import load_model
from imutils import build_montages
from imutils import paths
import numpy as np
import argparse
import random
import cv2



def predict_image(imagePaths):
    # load the pre-trained network
    print("[INFO] loading pre-trained network...")
    model = load_model("pneumonia.model")
    # grab all image paths in the input directory and randomly sample them
    #random.shuffle(imagePaths)
    #imagePaths = imagePaths[:16]

    # initialize our list of results
    results = []

    # loop over our sampled image paths
    #for p in imagePaths:
        # load our original input image
    orig = cv2.imread(imagePaths)

    # pre-process our image by converting it from BGR to RGB channel
    # ordering (since our Keras mdoel was trained on RGB ordering),
    # resize it to 64x64 pixels, and then scale the pixel intensities
    # to the range [0, 1]
    image = cv2.cvtColor(orig, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (48, 48))
    image = image.astype("float") / 255.0

    # order channel dimensions (channels-first or channels-last)
    # depending on our Keras backend, then add a batch dimension to
    # the image
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)

    # make predictions on the input image
    pred = model.predict(image)
    
    i = pred.argmax(axis=1)[0]
    
    
    #print(procent.shape())

    # an index of zero is the 'parasitized' label while an index of
    # one is the 'uninfected' label
    #pr_label = "(%.2f)" % procent
    label = "Pneumonia is detected" if i == 1 else "Pneumonia is not detected"
    color = (0, 0, 255) if i == 0 else (255, 0, 0)

    #label = label + pr_label
    text = "{}: {:.2f}%".format(label, pred[0][i]*100)

    # resize our original input (so we can better visualize it) and
    # then draw the label on the image
    orig = cv2.resize(orig, (600, 600))
    cv2.putText(orig, text, (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1,
                color, 3)

    # add the output image to our list of resultss
    results.append(orig)
    # create a montage using 128x128 "tiles" with 4 rows and 4 columns
    # montage = build_montages(results, (1024, 1024, (1, 1))[0])

    # returns image so parent app can show it itself
    return orig

    # show the output montage
    #cv2.imshow("Results", orig)
    #cv2.waitKey(0)

