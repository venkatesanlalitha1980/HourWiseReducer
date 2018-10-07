#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 16:10:50 2018

@author: venkatesansubramanian
"""

import json
import csv

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

urlSegDicts = {}
avgRespDicts = {}
with open('data.json') as f:
    data = json.load(f)
path = data['InputPath']
writePath = data['writePath']
writePath1 = data['urlCountPath']
URLPath = data['URLPath']

with open(writePath, newline='') as csvFile:
    reader = csv.DictReader(csvFile)
    for row in reader:
        fileName = row['FileName']
        dateValue = row['DateValue']
        hourValue = row['HourValue']
        hitsValue = row['HitsCount']
        print(fileName + ' ' + dateValue + ' ' + hourValue + ' ' + hitsValue)
        
        txtFile = open(path + fileName, "r", encoding = "latin-1")
        for line in txtFile:
            singleLineSplit = line.split()
            if(len(singleLineSplit) > 12):
                f_dateValue = singleLineSplit[0]
                f_timeValue = singleLineSplit[1]
                f_timeValueSplit = f_timeValue.split(':')
                f_hourValue = f_timeValueSplit[0]
                f_Url = singleLineSplit[4]
                if(is_number(singleLineSplit[13])):
                    avgTime = int(singleLineSplit[13])
                else:
                    avgTime = 0
                if(is_number(f_hourValue)):
                    f_hourValue = int(f_hourValue)
                if(f_hourValue == int(hourValue)):
                    if(fileName + '__' + dateValue + '__' + hourValue + '__' + f_Url) in urlSegDicts:
                        urlSegDicts[fileName + '__' + dateValue + '__' + hourValue + '__' + f_Url] = urlSegDicts[fileName + '__' + dateValue + '__' + hourValue + '__' + f_Url] + 1
                        avgRespDicts[fileName + '__' + dateValue + '__' + hourValue + '__' + f_Url] = avgRespDicts[fileName + '__' + dateValue + '__' + hourValue + '__' + f_Url] + avgTime
                    else:
                        urlSegDicts[fileName + '__' + dateValue + '__' + hourValue + '__' + f_Url] = 1
                        avgRespDicts[fileName + '__' + dateValue + '__' + hourValue + '__' + f_Url] = avgTime
        txtFile.close()
        
for k,v in avgRespDicts.items():
    avgRespDicts[k] = round(avgRespDicts[k]/urlSegDicts[k],2)
    
newFile = open(URLPath, 'w', encoding='latin-1')
for k,v in urlSegDicts.items():
    kSplit = str(k).split('__')
    newFile.write(kSplit[0] + ',' + kSplit[1] + ',' + kSplit[2] + ',' + kSplit[3] + ',' + str(v) + '\n')
newFile.close()

newFile = open(writePath1, 'w', encoding='latin-1')
for k,v in avgRespDicts.items():
    kSplit = str(k).split('__')
    newFile.write(kSplit[0] + ',' + kSplit[1] + ',' + kSplit[2] + ',' + kSplit[3] + ',' + str(v) + '\n')
newFile.close()