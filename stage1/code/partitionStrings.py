#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 17:25:33 2018

@author: yashtrivedi
"""

import os
import sys
import random
import string
from sets import Set
from sklearn import tree
from sklearn import svm
from sklearn import linear_model
from sklearn.model_selection import GridSearchCV
from sklearn.cross_validation import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score, recall_score
from sklearn.feature_selection import mutual_info_regression
from collections import Counter

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

oBasePath = '/Users/yashtrivedi/cs839/dataset_original'
oTrainPath = '/Users/yashtrivedi/cs839/train_original'
oTestPath = '/Users/yashtrivedi/cs839/test_original'
oExtraPath = '/Users/yashtrivedi/cs839/extra_original'

namePath = '/Users/yashtrivedi/cs839/name.txt'
occupationsPath = '/Users/yashtrivedi/cs839/occupations.txt'
prepositionsPath = '/Users/yashtrivedi/cs839/prepositions.txt'
conjunctionsPath = '/Users/yashtrivedi/cs839/conjunctions.txt'
pronounsPath = '/Users/yashtrivedi/cs839/pronouns.txt'
prefixPath = '/Users/yashtrivedi/cs839/prefix.txt'
suffixPath = '/Users/yashtrivedi/cs839/Suffixes.txt'
commanNamePath = '/Users/yashtrivedi/cs839/PopularNames.txt'
wordsPath = '/Users/yashtrivedi/cs839/words.txt'
bagOfWordsPath = '/Users/yashtrivedi/cs839/bow.txt'
countriesPath = '/Users/yashtrivedi/cs839/countries.txt'

class TrainingItem:
    string = 0
    docid = 0
    startpos = 0
    endpos = 0
    length = 0
    distPrefix = 0 
    distSuffix = 0 
    distOccupation = 0
    distNumeric = 0
    containsCommonName = 0
    containsApostrophe = 0
    label = 10
    isWord = 0
    normFreq = 0.0
    nWords = 0
    isUpperNext = 0
    
names = Set()
occupations = Set()
prepositions = Set()
conjunctions = Set()
pronouns = Set()
prefixes = Set()
suffixes = Set()
commonNames = Set()
dictWords = Set()
countries = Set()
whitelist = Set()

bagOfWords = []
bagOfWordsDict = {}
words = []

nameFile = open(namePath, 'r')
for line in nameFile:
    line = line.replace('\n', '')
    names.add(line)
    nameparts = line.split(' ')
    for x in nameparts:
        x = x.replace('\n', '')
        names.add(x)
        
occupationFile = open(occupationsPath, 'r')
for line in occupationFile:
    line = line.replace('\n','')
    occupations.add(line.lower())

prepositionFile = open(prepositionsPath, 'r')
for line in prepositionFile:
    line = line.replace('\n','')
    prepositions.add(line.lower())
    
conjunctionFile = open(conjunctionsPath, 'r')
for line in conjunctionFile:
    line = line.replace('\n','')
    conjunctions.add(line.lower())
    
pronounFile = open(pronounsPath, 'r')
for line in pronounFile:
    line = line.replace('\n','')
    pronouns.add(line.lower())

prefixFile = open(prefixPath, 'r')
for line in prefixFile:
    line = line.replace('\n','')
    prefixes.add(line.lower())
    
suffixFile = open(suffixPath, 'r')
for line in suffixFile:
    line = line.replace('\n','')
    suffixes.add(line.lower())
    
commanNameFile = open(commanNamePath, 'r')
for line in commanNameFile:
    line = line.replace('\n','')
    commonNames.add(line.lower())
    
wordsFile = open(wordsPath, 'r')
for line in wordsFile:
    line = line.replace(' ','')
    line = line.replace('\n','')
    dictWords.add(line.lower())
    
countriesFile = open(countriesPath, 'r')
for line in countriesFile:
    line = line.replace(' ','')
    line = line.replace('\n','')
    countries.add(line.lower())

total = int(0)
bagOfWordsFile = open(bagOfWordsPath, 'r')
for line in bagOfWordsFile:
    line = line.strip()
    line = line.replace('\n','')
    word, count = line.split(' ')
    word = word.lower()
    count = int(count)
    total += count
    bagOfWords.append(word)
    bagOfWordsDict[word] = count

PFileList = Set()
QFileList = Set()

fileList = os.listdir(oTrainPath)

while len(PFileList) < 195:
    PFileList.add(fileList[random.randint(0, len(fileList) - 1)])

for i in fileList:
    if i not in PFileList:
        QFileList.add(i)

processed = []
Pprocessed = []
Qprocessed = []

for i in fileList:
    if ((i in PFileList) and (i in QFileList)):
        print 'ERROR: ' + i

for fileName in fileList:
    
    one = []
    two = []
    three = []
    four = []
    everything = []
    
    prefixPos = []
    suffixPos = []
    occupationPos = []
    numericPos = []
    
    f = open(oTrainPath + '/' + fileName, 'r')
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
    
    orgFileName = fileName
    fileName = int(fileName.replace('.txt',''))
    pos = int(0)
    for word in words:
        word = word.strip()
        if len(word) > 0:
            if word.lower() in prefixes:
                prefixPos.append(pos)
            if word.lower() in suffixes:
                suffixPos.append(pos)
            if word.lower() in occupations:
                occupationPos.append(pos)
            if RepresentsInt(word.lower()):
                numericPos.append(pos)
                
        pos += (len(word) + 1)
    
    pos = int(0)
    for word in words:
        word = word.strip()
        if len(word) > 0:
            item = TrainingItem()
            item.startpos = pos
            item.length = int(len(word))
            item.endpos = item.startpos + item.length
            item.docid = fileName
            item.string = word
            item.normFreq = (float(bagOfWordsDict[word.lower()]) / total)
            item.nWords = 1
            one.append(item)
            pos += (len(word) + 1)
            
    for x in one:
        minDist = sys.maxint
        for d in prefixPos:
            dist = min(abs(x.startpos - d), abs(x.endpos - d))
            if dist < minDist:
                minDist = dist
        #x.distPrefix = minDist
        
        minDist = sys.maxint
        for d in suffixPos:
            dist = min(abs(x.startpos - d), abs(x.endpos - d))
            if dist < minDist:
                minDist = dist
        #x.distSuffix = minDist
        
        minDist = sys.maxint
        for d in occupationPos:
            dist = min(abs(x.startpos - d), abs(x.endpos - d))
            if dist < minDist:
                minDist = dist
        x.distOccupation = minDist
        
        minDist = sys.maxint
        for d in numericPos:
            dist = min(abs(x.startpos - d), abs(x.endpos - d))
            if dist < minDist:
                minDist = dist
        x.distNumeric = minDist
        
        if x.string.lower() in dictWords:
            x.isWord = 1
        else:
            x.isWord = 0
            
    for i in range(1, len(one)):
        if(one[i-1].string.lower() in prefixes):
            one[i].distPrefix = 1
        else:
            one[i].distPrefix = 0
            
    for i in range(0, len(one) - 1):
        if(one[i+1].string.lower() in suffixes):
            one[i].distSuffix = 1
        else:
            one[i].distSuffix = 0
            
        if(one[i+1].string.istitle()):
            one[i].isUpperNext = 1
            
    for i in range(len(words) - 1):
        item = TrainingItem()
        s = words[i].strip() + ' ' + words[i+1].strip()
        item.string = s
        item.startpos = one[i].startpos
        item.endpos = one[i+1].endpos
        item.length = int(len(s))
        item.docid = fileName
        item.distOccupation = min(one[i].distOccupation, one[i+1].distOccupation)
        item.isWord = (one[i].isWord or one[i+1].isWord)
        item.normFreq = one[i].normFreq + one[i+1].normFreq
        item.nWords = 2
        if i > 0:
            if(one[i-1].string.lower() in prefixes):
                item.distPrefix = 1
            else:
                item.distPrefix = 0
        
        if i < len(words) - 2:
            if(one[i+2].string.lower() in suffixes):
                item.distSuffix = 1
            else:
                item.distSuffix = 0
            if(one[i+2].string.istitle()):
                item.isUpperNext = 1
            
            
        two.append(item)
    
    for i in range(len(words) - 2):
        s = words[i].strip() + ' ' + words[i+1].strip() + ' ' + words[i+2].strip()
        item = TrainingItem()
        item.string = s
        item.startpos = one[i].startpos
        item.endpos = one[i+2].endpos
        item.length = len(s)
        item.docid = fileName
        item.distOccupation = min(one[i].distOccupation, one[i+1].distOccupation, one[i+2].distOccupation)
        item.isWord = (one[i].isWord or one[i+1].isWord or one[i+2].isWord)
        item.normFreq = one[i].normFreq + one[i+1].normFreq + one[i+2].normFreq
        item.nWords = 3
        if i > 0:
            if(one[i-1].string.lower() in prefixes):
                item.distPrefix = 1
            else:
                item.distPrefix = 0
        
        if i < len(words) - 3:
            if(one[i+3].string.lower() in suffixes):
                item.distSuffix = 1
            else:
                item.distSuffix = 0
            if(one[i+3].string.istitle()):
                item.isUpperNext = 1
        three.append(item)
        
    for x in one:
        everything.append(x)
    
    for x in two:
        everything.append(x)
        
    for x in three:
        everything.append(x)
        
    for x in everything:
        if(x.string.find("'") != -1):
            x.containsApostrophe = 1
        else:
            x.containsApostrophe = 0
            
        s = x.string.split(' ')
        flag = False
        for i in s:
            iLower = i.lower()
            if iLower in occupations or iLower in prepositions or iLower in conjunctions or iLower in pronouns or RepresentsInt(iLower) or iLower in countries or any(char in set(string.punctuation) for char in iLower):
                flag = True
        
        if not x.string.istitle():
            flag = True
            
        nameFlag = False
        for i in s:
            iLower = i.lower()
            if iLower not in commonNames:
                nameFlag = True
        
        if(not nameFlag):
            x.containsCommonName = 1
        else:
            x.containsCommonName = 0
        
        if(x.distOccupation < 20):
            x.distOccupation = 1
        else:
            x.distOccupation = 0
            
        if(not flag):
            processed.append(x)
        if(not flag and orgFileName in PFileList):
            Pprocessed.append(x)
        if(not flag and orgFileName in QFileList):
            Qprocessed.append(x)
            

posCount = int(0)
negCount = int(0)

for i in processed:
    if i.string in names:
        i.label = 1
        posCount += 1
    else:
        i.label = 0
        negCount += 1
        
X = []
Y_true = []
Y_pred = []

idx = int(0)
for i in processed:
    tempList = []
    #tempList.append(i.docid)
    #tempList.append(i.startpos)
    #tempList.append(i.endpos)
    tempList.append(i.length)
    tempList.append(i.distPrefix)
    tempList.append(i.distSuffix)
    #tempList.append(i.distOccupation)
    #tempList.append(i.distNumeric)
    tempList.append(i.containsCommonName)
    #tempList.append(i.containsApostrophe)
    tempList.append(i.isWord)
    tempList.append(i.normFreq)
    tempList.append(i.nWords)
    #tempList.append(i.isUpperNext)
    
    X.append(tempList)
    Y_true.append(i.label)
    idx += 1

X_P = []
X_Q = []
Y_P = []
Y_Q = []

for i in Pprocessed:
    tempList = []
    tempList.append(i.docid)
    #tempList.append(i.startpos)
    #tempList.append(i.endpos)
    tempList.append(i.length)
    tempList.append(i.distPrefix)
    tempList.append(i.distSuffix)
    #tempList.append(i.distOccupation)
    #tempList.append(i.distNumeric)
    tempList.append(i.containsCommonName)
    tempList.append(i.containsApostrophe)
    tempList.append(i.isWord)
    tempList.append(i.normFreq)
    tempList.append(i.nWords)
    
    X_P.append(tempList)
    Y_P.append(i.label)
    
for i in Qprocessed:
    tempList = []
    tempList.append(i.docid)
    tempList.append(i.startpos)
    tempList.append(i.endpos)
    tempList.append(i.length)
    tempList.append(i.distPrefix)
    tempList.append(i.distSuffix)
    tempList.append(i.distOccupation)
    #tempList.append(i.distNumeric)
    tempList.append(i.containsCommonName)
    tempList.append(i.containsApostrophe)
    tempList.append(i.isWord)
    tempList.append(i.normFreq)
    tempList.append(i.nWords)
    
    X_Q.append(tempList)
    Y_Q.append(i.label)
    
#print len(X), len(X_P), len(X_Q), len(Y_true), len(Y_P), len(Y_Q)

dt = tree.DecisionTreeClassifier()
rf = RandomForestClassifier()
svc = svm.SVC()
logreg = linear_model.LogisticRegression()

param_grid = {"criterion": ["entropy"],
              "min_samples_split": [2, 10, 20],
              "max_depth": [None, 2, 5, 10],
              "min_samples_leaf": [1, 5, 10],
              "max_leaf_nodes": [None, 5, 10, 20],
              }

parameters = {'kernel':('linear', 'rbf'), 'C':[1, 10]}

params = {'C':[0.000001, 0.00001, 0.0001, 0.001, 0.01, 0.1, 1, 10, 100, 1000], 'solver':['newton-cg', 'lbfgs', 'liblinear', 'sag', 'saga'], 'max_iter':[1000, 5000, 10000]}

# =============================================================================
# mi = mutual_info_regression(X, Y_true)
# print mi
# =============================================================================

clf = GridSearchCV(dt, param_grid=param_grid, cv=10)
clf.fit(X, Y_true)
Y_pred = clf.predict(X)
print precision_score(Y_true, Y_pred), recall_score(Y_true, Y_pred)

# =============================================================================
# clf = GridSearchCV(svc, parameters)
# clf.fit(X, Y_true)
# Y_pred = clf.predict(X)
# =============================================================================

# =============================================================================
# clf = GridSearchCV(logreg, params)
# clf.fit(X, Y_true)
# Y_pred = clf.predict(X)
# =============================================================================

processed = []

fileList = os.listdir(oTestPath)
for fileName in fileList:
    
    one = []
    two = []
    three = []
    four = []
    everything = []
    
    prefixPos = []
    suffixPos = []
    occupationPos = []
    numericPos = []
    
    f = open(oTestPath + '/' + fileName, 'r')
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
    
    orgFileName = fileName
    fileName = int(fileName.replace('.txt',''))
    pos = int(0)
    for word in words:
        word = word.strip()
        if len(word) > 0:
            if word.lower() in prefixes:
                prefixPos.append(pos)
            if word.lower() in suffixes:
                suffixPos.append(pos)
            if word.lower() in occupations:
                occupationPos.append(pos)
            if RepresentsInt(word.lower()):
                numericPos.append(pos)
                
        pos += (len(word) + 1)
    
    pos = int(0)
    for word in words:
        word = word.strip()
        if len(word) > 0:
            item = TrainingItem()
            item.startpos = pos
            item.length = int(len(word))
            item.endpos = item.startpos + item.length
            item.docid = fileName
            item.string = word
            item.normFreq = (float(bagOfWordsDict[word.lower()]) / total)
            item.nWords = 1
            one.append(item)
            pos += (len(word) + 1)
            
    for x in one:
        minDist = sys.maxint
        for d in prefixPos:
            dist = min(abs(x.startpos - d), abs(x.endpos - d))
            if dist < minDist:
                minDist = dist
        #x.distPrefix = minDist
        
        minDist = sys.maxint
        for d in suffixPos:
            dist = min(abs(x.startpos - d), abs(x.endpos - d))
            if dist < minDist:
                minDist = dist
        #x.distSuffix = minDist
        
        minDist = sys.maxint
        for d in occupationPos:
            dist = min(abs(x.startpos - d), abs(x.endpos - d))
            if dist < minDist:
                minDist = dist
        x.distOccupation = minDist
        
        minDist = sys.maxint
        for d in numericPos:
            dist = min(abs(x.startpos - d), abs(x.endpos - d))
            if dist < minDist:
                minDist = dist
        x.distNumeric = minDist
        
        if x.string.lower() in dictWords:
            x.isWord = 1
        else:
            x.isWord = 0
            
    for i in range(1, len(one)):
        if(one[i-1].string.lower() in prefixes):
            one[i].distPrefix = 1
        else:
            one[i].distPrefix = 0
            
    for i in range(0, len(one) - 1):
        if(one[i+1].string.lower() in suffixes):
            one[i].distSuffix = 1
        else:
            one[i].distSuffix = 0
            
        if(one[i+1].string.istitle()):
            one[i].isUpperNext = 1
            
    for i in range(len(words) - 1):
        item = TrainingItem()
        s = words[i].strip() + ' ' + words[i+1].strip()
        item.string = s
        item.startpos = one[i].startpos
        item.endpos = one[i+1].endpos
        item.length = int(len(s))
        item.docid = fileName
        item.distOccupation = min(one[i].distOccupation, one[i+1].distOccupation)
        item.isWord = (one[i].isWord or one[i+1].isWord)
        item.normFreq = one[i].normFreq + one[i+1].normFreq
        item.nWords = 2
        if i > 0:
            if(one[i-1].string.lower() in prefixes):
                item.distPrefix = 1
            else:
                item.distPrefix = 0
        
        if i < len(words) - 2:
            if(one[i+2].string.lower() in suffixes):
                item.distSuffix = 1
            else:
                item.distSuffix = 0
            if(one[i+2].string.istitle()):
                item.isUpperNext = 1
            
            
        two.append(item)
    
    for i in range(len(words) - 2):
        s = words[i].strip() + ' ' + words[i+1].strip() + ' ' + words[i+2].strip()
        item = TrainingItem()
        item.string = s
        item.startpos = one[i].startpos
        item.endpos = one[i+2].endpos
        item.length = len(s)
        item.docid = fileName
        item.distOccupation = min(one[i].distOccupation, one[i+1].distOccupation, one[i+2].distOccupation)
        item.isWord = (one[i].isWord or one[i+1].isWord or one[i+2].isWord)
        item.normFreq = one[i].normFreq + one[i+1].normFreq + one[i+2].normFreq
        item.nWords = 3
        if i > 0:
            if(one[i-1].string.lower() in prefixes):
                item.distPrefix = 1
            else:
                item.distPrefix = 0
        
        if i < len(words) - 3:
            if(one[i+3].string.lower() in suffixes):
                item.distSuffix = 1
            else:
                item.distSuffix = 0
            if(one[i+3].string.istitle()):
                item.isUpperNext = 1
        three.append(item)
        
    for x in one:
        everything.append(x)
    
    for x in two:
        everything.append(x)
        
    for x in three:
        everything.append(x)
        
    for x in everything:
        if(x.string.find("'") != -1):
            x.containsApostrophe = 1
        else:
            x.containsApostrophe = 0
            
        s = x.string.split(' ')
        flag = False
        for i in s:
            iLower = i.lower()
            if iLower in occupations or iLower in prepositions or iLower in conjunctions or iLower in pronouns or RepresentsInt(iLower) or iLower in countries or any(char in set(string.punctuation) for char in iLower):
                flag = True
        
        if not x.string.istitle():
            flag = True
            
        nameFlag = False
        for i in s:
            iLower = i.lower()
            if iLower not in commonNames:
                nameFlag = True
        
        if(not nameFlag):
            x.containsCommonName = 1
        else:
            x.containsCommonName = 0
        
        if(x.distOccupation < 20):
            x.distOccupation = 1
        else:
            x.distOccupation = 0
            
        if(not flag):
            processed.append(x)
        if(not flag and orgFileName in PFileList):
            Pprocessed.append(x)
        if(not flag and orgFileName in QFileList):
            Qprocessed.append(x)
            

posCount = int(0)
negCount = int(0)

for i in processed:
    if i.string in names:
        i.label = 1
        posCount += 1
    else:
        i.label = 0
        negCount += 1

X = []
Y_true = []
Y_pred = []

idx = int(0)
for i in processed:
    tempList = []
    #tempList.append(i.docid)
    #tempList.append(i.startpos)
    #tempList.append(i.endpos)
    tempList.append(i.length)
    tempList.append(i.distPrefix)
    tempList.append(i.distSuffix)
    #tempList.append(i.distOccupation)
    #tempList.append(i.distNumeric)
    tempList.append(i.containsCommonName)
    #tempList.append(i.containsApostrophe)
    tempList.append(i.isWord)
    tempList.append(i.normFreq)
    tempList.append(i.nWords)
    #tempList.append(i.isUpperNext)
    
    #print i.distPrefix, i.distSuffix
    X.append(tempList)
    Y_true.append(i.label)
    idx += 1
    
incorrect = []

Y_pred = clf.predict(X)
        
print precision_score(Y_true, Y_pred), recall_score(Y_true, Y_pred)