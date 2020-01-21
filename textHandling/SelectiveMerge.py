# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 05:41:43 2020

@author: nate

Choose an extract of one file and merge into a base file based on file data.
"""

import os
import pandas

INPUT_DIR = "D:\python-course-files"
LEFT_FILE = os.path.join(INPUT_DIR, "IncomeByStateByYearUnique.csv")
RIGHT_FILE = os.path.join(INPUT_DIR, "station-info.txt")
OUTPUT_FILE = os.path.join(INPUT_DIR,  "exercises-output", "ConcatenatedMerged.csv")

def merge(left = LEFT_FILE, right = RIGHT_FILE, out = OUTPUT_FILE):
    leftDf = pandas.read_csv(left)
    
    # dict to contain column conversion spec
    converterDict = { "USAF": str, "WBAN": str }
    # read in file & convert column data to string for creating new field
    rightDf = pandas.read_fwf(right, converters=converterDict)
    # add new column which matches our left ID column
    rightDf["USAF_WBAN"] = rightDf["USAF"] + '-' + rightDf["WBAN"]
    """
    Merge files horizontally. We want:
        - the entire left file
        - slice of right file using ix
            - first param specifies all rows, second specifies columns to grab
    """
    mergedDf = pandas.merge(leftDf, rightDf.ix[:, ["USAF_WBAN", "STATION NAME","LAT", "LON"]], left_on="ID", right_on="USAF_WBAN")
    
    # output
    mergedDf.to_csv(out)