# DiseaseDetection
![](https://img.shields.io/github/license/pandao/editor.m..)
# About
This project containing a convolutional neural network that is capable to predict breast cancer in breast histology images and pneumonia in lungs x-rays. It was based on a simplified VGGNet model with 3 convolutional layers. The project includes a trained model and prediction function.

The architecture of the neural network is shown in the picture:

![Architecture](https://github.com/AnneVR/DiseaseDetection/blob/main/report/Architecture.png)

This neural network was trained on 277524 images of breast histology and 5863 images of lungs x-rays. In the process of training we have achieved an accuracy of about 95% percent:

![training_results](https://github.com/AnneVR/DiseaseDetection/blob/main/report/training_results.jpg)

# Sample Data Sources
We used the following sample data to train and test the neural network:
## Breast Histopathology Images
This dataset consisted of 162 whole mount slide images of breast сancer specimens scanned at 40x. From that, 277,524 patches of size 50 x 50 were extracted (198,738 IDC negative and 78,786 IDC positive). Each patch’s file name is of the format: u_xX_yY_classC.png — > example 10253_idx5_x1351_y1101_class0.png . Where u is the patient ID (10253_idx5), X is the x-coordinate of where this patch was cropped from, Y is the y-coordinate of where this patch was cropped from, and C indicates the class where 0 is non-identified and 1 is identified.

The dataset can be found here: https://www.kaggle.com/paultimothymooney/breast-histo..

## Chest X-Ray Images (Pneumonia)
The dataset is divided into training and testing parts, each of which contains x-rays, where the disease is identified(PNEUMONIA folder) and where it is not (NORMAL folder).

The dataset can be found here: https://www.kaggle.com/paultimothymooney/chest-xray-p..

# Installation
To use this project, you will need Python >= 3.3 and some additional libraries:
- Tensorflow 1.14.0
- Keras
- OpenCV
- Matplotlib
- Pickle
- Numpy

# Basic usage
## Breast cancer identification
To use this neural network, you need a png/jpeg picture of breast histology. Using the GUI, you can upload your image, and the result of the program will appear in a new window.

For example, you can use this ‘hystology+.jpg’ picture, which depicts the histology with identified cancer:

![hystology+](https://github.com/AnneVR/DiseaseDetection/blob/main/report/hystology%2B.jpg)

Using the program you can get the result of neural network prediction:

![result_cancer_61-98](https://github.com/AnneVR/DiseaseDetection/blob/main/report/result_cancer_61-98.png)

As a result of this function, you get the neural network prediction regarding this image. As you can see, the cancer was correctly identified.

## Pneumonia identification
To use this neural network, you need a png/jpeg picture of lungs x-ray. Using the GUI, you can upload your image, and the result of the program will appear in a new window.

For example, you can use this ‘xray-lungs.jpg’ picture, which depicts the histology with identified cancer:

![xray-lungs](https://github.com/AnneVR/DiseaseDetection/blob/main/report/xray-lungs.jpg)

Using the program you can get the result of neural network prediction:

![Results_screenshot_222](https://github.com/AnneVR/DiseaseDetection/blob/main/report/Results_screenshot_222.png)

As a result of this function, you get the neural network prediction regarding this image. As you can see, the pneumonia was correctly identified.

# License
This project is licensed under the terms of the MIT license, see LICENSE.
