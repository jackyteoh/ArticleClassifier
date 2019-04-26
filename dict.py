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
d = len(words) # Number of features (unique words) we have in the dictionary
# print(d)
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

#Target Training Vector
train_y = [0] * 1561
for i in range(358, 1561):
	if i >= 358 and i < 628:
		train_y[i] = 1
	elif i >= 628 and i < 921:
		train_y[i] = 2
	elif i >= 921 and i < 1280:
		train_y[i] = 3
	elif i >= 1280 and i < 1561:
		train_y[i] = 4

#Create Testing Data Matrix
test_x = []

testfile = open("testTextFile.txt", "r")

for line in testfile:
	line = line.replace("'", "")
	word = line.split()
	arr = [0] * d
	for i in word:
		if i in words:
			index = words[i]
			arr[index] = arr[index] + 1
	test_x.append(arr)
testfile.close()

#Target Test Vector
test_y = [0] * 664
for i in range(152, 664):
	if i >= 152 and i < 268:
		test_y[i] = 1
	elif i >= 268 and i < 392:
		test_y[i] = 2
	elif i >= 392 and i < 544:
		test_y[i] = 3
	elif i >= 544 and i < 664:
		test_y[i] = 4

countzero = 0
countone = 0
counttwo = 0
countthree = 0
countfour = 0
for i in test_y:
	if i == 0:
		countzero+=1
	if i == 1:
		countone += 1
	if i == 2:
		counttwo+=1 
	if i == 3:
		countthree+=1
	if i == 4:
		countfour +=1

print(countzero)
print(countone)
print(counttwo)
print(countthree)
print(countfour)


# y = 0 --> Business
# y = 1 --> Entertainment
# y = 2 --> Politics
# y = 3 --> Sport
# y = 4 --> Tech





		