#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 08:08:34 2018

@author: venkatesansubramanian
"""

import json
import os

dayHourDicts = {}

with open('data.json') as f:
    data = json.load(f)
path = data['InputPath']
writePath = data['writePath']
dirs = os.listdir(path)
for fileName in dirs:
    txtFile = open(path + fileName, "r", encoding="latin-1")
    for line in txtFile:
        singleLineSplit = line.split()
        if(len(singleLineSplit) > 10):
            dataValue = singleLineSplit[0]
            timeValue = singleLineSplit[1]
            timeValueSplit = timeValue.split(':')
            hourValue = timeValueSplit[0]
            if (fileName + " " + dataValue + " " + hourValue) in dayHourDicts:
                dayHourDicts[fileName + " " + dataValue + " " + hourValue] = dayHourDicts[fileName + " " + dataValue + " " + hourValue] + 1
            else:
                dayHourDicts[fileName + " " + dataValue + " " + hourValue] = 1
    txtFile.close()
newFile = open(writePath, 'w', encoding = "latin-1")
for k,v in dayHourDicts.items():
    kSplit = str(k).split()
    newFile.write(kSplit[0] + "," + kSplit[1] + "," + kSplit[2] + "," + str(v) + '\n')
newFile.close()