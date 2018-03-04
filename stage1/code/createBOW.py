#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 13:54:07 2018

@author: yashtrivedi
"""
import os
from sets import Set

oTrainPath = '/Users/yashtrivedi/cs839/train_original'
oTestPath = '/Users/yashtrivedi/cs839/test_original'
bagOfWordsPath = '/Users/yashtrivedi/cs839/bow.txt'

bagOfWords = Set()
bagOfWordsList = []

fileList = os.listdir(oBasePath)
for fileName in fileList:
    f = open(oBasePath + '/' + fileName, 'r')
    s = f.read()
    s = s.replace('\n', ' ')
    s = s.replace('\r', ' ')
    s = s.replace(',', '')
    s = s.replace('.', '')
    s = s.replace(';', '')
    s = s.replace(':', '')
    s = s.replace('(', '')
    s = s.replace(')', '')
    s = s.replace('[', '')
    s = s.replace(']', '')
    s = s.replace('"', '')
    s = s.replace('-', '')
    
    s = " ".join(s.split())
    words = s.split(' ')
    
    for word in words:
        word = word.strip()
        if len(word) > 0:
            bagOfWords.add(word.lower())
            bagOfWordsList.append(word.lower())

bagOfWordsFile = open(bagOfWordsPath, 'a')
for word in bagOfWords:
    bagOfWordsFile.write(word + ' ' + str(bagOfWordsList.count(word)) + '\n')
    
bagOfWordsFile.close()
