#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 03:13:15 2018

@author: yashtrivedi
"""

import os
import re

trainPath = '/Users/yashtrivedi/cs839/train'
testPath = '/Users/yashtrivedi/cs839/test'

namePath = '/Users/yashtrivedi/cs839/name.txt'
prefixPath = '/Users/yashtrivedi/cs839/prefix.txt'
suffixPath = '/Users/yashtrivedi/cs839/suffix.txt'

nameFile = open(namePath, 'a')
prefixFile = open(prefixPath, 'a')
suffixFile = open(suffixPath, 'a')

fileList = os.listdir(trainPath)
for fileName in fileList:
    f = open(trainPath + '/' + fileName, 'r')
    s = f.read()
    regexp_name = re.compile(r'(<n>(.*?)</n>)')
    regexp_prefix = re.compile(r'(<p>(.*?)</p>)')
    regexp_suffix = re.compile(r'(<s>(.*?)</s>)')
    
    match_name = regexp_name.findall(s)
    match_prefix = regexp_prefix.findall(s)
    match_suffix = regexp_suffix.findall(s)
    
    for i in range(len(match_name)):
        nameFile.write(str(match_name[i][1]) + '\n')
    for i in range(len(match_prefix)):
        prefixFile.write(str(match_prefix[i][1]) + '\n')
    for i in range(len(match_suffix)):
        suffixFile.write(str(match_suffix[i][1]) + '\n')
        
fileList = os.listdir(testPath)
for fileName in fileList:
    f = open(testPath + '/' + fileName, 'r')
    s = f.read()
    regexp_name = re.compile(r'(<n>(.*?)</n>)')
    regexp_prefix = re.compile(r'(<p>(.*?)</p>)')
    regexp_suffix = re.compile(r'(<s>(.*?)</s>)')
    
    match_name = regexp_name.findall(s)
    match_prefix = regexp_prefix.findall(s)
    match_suffix = regexp_suffix.findall(s)
    
    for i in range(len(match_name)):
        nameFile.write(str(match_name[i][1]) + '\n')
    for i in range(len(match_prefix)):
        prefixFile.write(str(match_prefix[i][1]) + '\n')
    for i in range(len(match_suffix)):
        suffixFile.write(str(match_suffix[i][1]) + '\n')

nameFile.close()
prefixFile.close()
suffixFile.close()
    