import os
import numpy as np
import re

training = []
testing = []

# Puts words in dictionary, key = word, value = index
trfile = open("trainingTextFile.txt", "r")

for line in trfile:
	line = line.replace("'", "")
	new_line = line.split()
	for i in new_line:
		training.append(i)

trfile.close()

words = {}
count = 0
for i in training:
	if i not in words:
		words[i] = count
		count = count + 1

#Create Training Data Matrix
d = len(words)
print(d)
train_x = []

trfile = open("trainingTextFile.txt", "r")

for line in trfile:
	line = line.replace("'", "")
	word = line.split()
	arr = [0] * d
	for i in word:
		index = words[i]
		arr[index] = arr[index] + 1
	train_x.append(arr)
trfile.close()

#Target Vector
train_y = [0] * 1000
for i in range(200, 1000):
	if i >= 200 and i < 400:
		train_y[i] = 1
	elif i >= 400 and i < 600:
		train_y[i] = 2
	elif i >= 600 and i < 800:
		train_y[i] = 3
	elif i >= 800 and i < 1000:
		train_y[i] = 4

# y = 0 --> Business
# y = 1 --> Entertainment
# y = 2 --> Politics
# y = 3 --> Sport
# y = 4 --> Tech





		