#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 05:00:55 2018

@author: yashtrivedi
"""

import os
from shutil import copyfile

basePath = '/Users/yashtrivedi/cs839/dataset'
trainPath = '/Users/yashtrivedi/cs839/train'
testPath = '/Users/yashtrivedi/cs839/test'
extraPath = '/Users/yashtrivedi/cs839/extra'

oBasePath = '/Users/yashtrivedi/cs839/dataset_original'
oTrainPath = '/Users/yashtrivedi/cs839/train_original'
oTestPath = '/Users/yashtrivedi/cs839/test_original'
oExtraPath = '/Users/yashtrivedi/cs839/extra_original'

os.remove('/Users/yashtrivedi/cs839/train/.DS_Store')

fileList = os.listdir(trainPath)
for fileName in fileList:
    copyfile(oBasePath + '/' + fileName, oTrainPath + '/' + fileName)
    
fileList = os.listdir(testPath)
for fileName in fileList:
    copyfile(oBasePath + '/' + fileName, oTestPath + '/' + fileName)
    
fileList = os.listdir(extraPath)
for fileName in fileList:
    copyfile(oBasePath + '/' + fileName, oExtraPath + '/' + fileName)