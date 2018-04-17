#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 20:44:21 2018

@author: yashtrivedi
"""

import pandas as pd

df = pd.read_csv('/Users/yashtrivedi/cs839-git/cs839/stage2/DATA/A.csv')
colsA = ['full name', 'name', 'club', 'nation', 'overall', 'league', 'age', 'height',
         'reactions', 'positioning', 'penalties', 'long passing', 'standing tackle',
         'ball control', 'interceptions', 'acceleration', 'marking', 'strength', 
         'pac', 'aggression', 'agility', 'volleys', 'sprint speed', 'phy', 'pas', 
         'sliding tackle', 'long_shots', 'short passing', 'shot power', 'curve', 'dri',
         'jumping', 'vision', 'crossing', 'finishing', 'balance', 'heading accuracy',
         'defending', 'sho', 'free kick accuracy', 'composure', 'foot', 'dribbling', 'stamina']

df = df[colsA]
df.to_csv('/Users/yashtrivedi/cs839ps3/A.csv', index=False)

df = pd.read_csv('/Users/yashtrivedi/cs839-git/cs839/stage2/DATA/B.csv')
colsB = ['full_name', 'name', 'club', 'nation', 'overall', 'league', 
        'age', 'height', 'reactions', 'positioning', 'penalties', 
        'long passing', 'standing tackle', 'ball control', 'interceptions', 
        'acceleration', 'marking', 'strength', 'pac', 'aggression', 'agility', 
        'volleys', 'sprint speed', 'phy', 'pas', 'sliding tackle', 'long shots',
        'short passing', 'shot power', 'curve', 'dri', 'jumping', 'vision',
        'crossing', 'finishing', 'balance', 'heading', 'def', 
        'sho', 'free kick', 'composure', 'strong foot', 'dribbling', 'stamina']

df = df[colsB]

df['full_name'] = df['full_name'].apply(lambda x: x.lower())
df['name'] = df['name'].apply(lambda x: x.lower())
df['club'] = df['club'].apply(lambda x: x.lower())
df['nation'] = df['nation'].apply(lambda x: x.lower())
df['league'] = df['league'].apply(lambda x: x.lower())
df['strong foot'] = df['strong foot'].apply(lambda x: x.lower())

df.to_csv('/Users/yashtrivedi/cs839ps3/B.csv', index=False)