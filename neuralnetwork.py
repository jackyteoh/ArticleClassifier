import os
import numpy as np 
from keras.models import Sequential
from keras.layers import Dense
from keras import optimizers

# epoch how many big loops
# batch = how many times each loop

# First model (smallest hidden layers (2))
model = Sequential()

model.add(Dense(units = d))

model.add(Dense(units = 500, activation = 'relu'))
model.add(Dense(units = 500, activation = 'relu'))

model.add(Dense(units = 5, activation = 'softmax'))


# Second model (Medium hidden layers (4))
model = Sequential()

model.add(Dense(units = d))

model.add(Dense(units = 500, activation = 'relu'))
model.add(Dense(units = 500, activation = 'relu'))
model.add(Dense(units = 500, activation = 'relu'))
model.add(Dense(units = 500, activation = 'relu'))

model.add(Dense(units = 5, activation = 'softmax'))


# Third model (Large hidden layers (6))
model = Sequential()

model.add(Dense(units = d))

model.add(Dense(units = 500, activation = 'relu'))
model.add(Dense(units = 500, activation = 'relu'))
model.add(Dense(units = 500, activation = 'relu'))
model.add(Dense(units = 500, activation = 'relu'))
model.add(Dense(units = 500, activation = 'relu'))
model.add(Dense(units = 500, activation = 'relu'))

model.add(Dense(units = 5, activation = 'softmax'))
model.summary()