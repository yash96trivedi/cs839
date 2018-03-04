#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 02:27:42 2018

@author: yashtrivedi
"""

import random
import os
from sets import Set
from shutil import copyfile

basePath = '/Users/yashtrivedi/cs839/dataset'
trainPath = '/Users/yashtrivedi/cs839/train'
testPath = '/Users/yashtrivedi/cs839/test'
extraPath = '/Users/yashtrivedi/cs839/extra'

train = Set()
test = Set()
extra = []

while len(train) != 200:
    x = random.randint(1, 330)
    train.add(x)
    
while len(test) != 100:
    x = random.randint(1, 330)
    if(x not in train):
        test.add(x)

for i in range(1, 331):
    if(i not in train and i not in test):
        extra.append(i)
        
fileList = os.listdir(trainPath)
for fileName in fileList:
    os.remove(trainPath + '/' + fileName)

fileList = os.listdir(testPath)
for fileName in fileList:
    os.remove(trainPath + '/' + fileName)
    
fileList = os.listdir(extraPath)
for fileName in fileList:
    os.remove(trainPath + '/' + fileName)

for i in train:
    fileName = "%03d" % (i, ) + str(".txt")
    copyfile(basePath + '/' + fileName, trainPath + '/' + fileName)
    
for i in test:
    fileName = "%03d" % (i, ) + str(".txt")
    copyfile(basePath + '/' + fileName, testPath + '/' + fileName)
    
for i in extra:
    fileName = "%03d" % (i, ) + str(".txt")
    copyfile(basePath + '/' + fileName, extraPath + '/' + fileName)
    
    
        
    
    