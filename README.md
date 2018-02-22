[![Udacity - Self-Driving Car NanoDegree](https://s3.amazonaws.com/udacity-sdc/github/shield-carnd.svg)](http://www.udacity.com/drive)

# CarND-Behavioral-Cloning
The goal of this project is to train a model to navigate a car around a simulated test track by Udacity.

![Car Simulation](https://github.com/Eleven-/CarND-Behavioral-Cloning/blob/master/examples/sim-image.png)

## Overview
1. Gather training data by running the simulator in training mode
2. Design a (CNN) model that takes image data and steering data to output a steering angle
3. Train and validate the model with a training and validation set
4. Test the model on the simulator and verify it can navigate safely around the track
5. Summarize the results in a report

## Installation
* Download [Simulator](https://d17h27t6h515a5.cloudfront.net/topher/2017/February/58ae4419_windows-sim/windows-sim.zip)
* Set up the [CarND Term1 Starter Kit](https://classroom.udacity.com/nanodegrees/nd013/parts/fbf77062-5703-404e-b60c-95b78b2f3f9e/modules/83ec35ee-1e02-48a5-bdb7-d244bd47c2dc/lessons/8c82408b-a217-4d09-b81d-1bda4c6380ef/concepts/4f1870e0-3849-43e4-b670-12e6f2d4b7a7) if you haven't already.
* Python 3 IDE

## Neural Network Model Architecture
1.	Convolution Layer 5x5, 24 depth, 2x2 RELU
2.	Convolution Layer 5x5, 36 depth, 2x2 RELU
3.	Convolution Layer 5x5, 48 depth, 2x2 RELU
4.	Convolution Layer 3x3, 64 depth
5.	Convolution Layer 3x3, 64 depth
6.	Flatten Layer
7.	Fully Connected Layer 400
8.	Fully Connected Layer 200
9.	Fully Connected Layer 100
10.	Fully Connected Layer 50
11.	Fully Connected Layer 10
12.	Fully Connected Layer 1
