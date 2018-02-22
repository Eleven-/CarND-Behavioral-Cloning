# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 13:22:56 2017

@author: Jdog
"""

import csv
import cv2
import numpy as np

lines = []
with open(r'C:\Users\Jdog\CarND-Behavioral-Cloning-P3-master/newest_data/driving_log.csv') as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        lines.append(line)
        
images = []
measurements = []
for line in lines:
    image = cv2.imread(line[0])
    images.append(image)
    measurement = float(line[3])
    measurements.append(measurement)

#augmented_images, augmented_measurements = [], []
#for image, measurement in zip(images, measurements):
#    augmented_images.append(image)
#    augmented_measurements.append(measurement)
#    augmented_images.append(cv2.flip(image, 1)) #Add Flipped Image
#    augmented_measurements.append(measurement*-1.0)

#convert from images to numpy.arrays
X_train = np.array(images)
y_train = np.array(measurements)
    
print('finished gathering images')    

from keras.models import Sequential
from keras.layers import Flatten, Dense, Lambda
from keras.layers import Convolution2D
from keras.layers import Cropping2D
from keras.layers import Dropout

#Regression Network

model = Sequential()
model.add(Lambda(lambda x: (x/255.0)-0.5, input_shape=(160,320,3))) #parallel image normalization
model.add(Cropping2D(cropping=((50,20), (0,0)), input_shape=(3,160,320)))

#Lenet
#model.add(Convolution2D(32))

model.add(Convolution2D(24,5,5,subsample=(2,2),activation="relu"))
model.add(Convolution2D(36,5,5,subsample=(2,2),activation="relu"))
model.add(Convolution2D(48,5,5,subsample=(2,2),activation="relu"))
model.add(Convolution2D(64,3,3,activation="relu"))
model.add(Convolution2D(64,3,3,activation="relu"))
#model.add(Convolution2D(32,5,5,activation="relu"))
#model.add(MaxPooling2D())

#model.add(Convolution2D(32,5,5,activation="relu"))
#model.add(MaxPooling2D())
model.add(Flatten())
model.add(Dense(400))
model.add(Dense(200))
model.add(Dense(100))
model.add(Dense(50))
model.add(Dense(10))
model.add(Dense(1)) #Single Output (Steering Measurement)

#mse instead of cross-entropy b/c of regression
model.compile(loss='mse', optimizer='adam')
#split data 0.8 training and 0.2 validation
model.fit(X_train, y_train, validation_split = 0.2, shuffle = True, nb_epoch = 2)

model.save('Jdog_model10.h5')