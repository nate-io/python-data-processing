# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 07:22:13 2020

@author: nate
"""

import os
import pandas

INPUT_DIR = "D:\python-course-files\exercises-output\income"
LEFT_FILE = os.path.join(INPUT_DIR, "IncomeByStateByYearUnique.csv")
RIGHT_FILE = os.path.join(INPUT_DIR, "geoids-states-lookup.csv")
OUTPUT_FILE = os.path.join(INPUT_DIR, "IncomeByStateByYearUniqueWithState.csv")

def exercise5(left = LEFT_FILE, right = RIGHT_FILE, out = OUTPUT_FILE):
    leftDf = pandas.read_csv(left)
    rightDf = pandas.read_csv(right)
    

    # merge on similar GEOIDS field
    mergedDf = pandas.merge(leftDf, rightDf, left_on="GEOID", right_on="GEOID")
    mergedDf.set_index(["GEOID", "State"], inplace=True)
    
    # output
    mergedDf.to_csv(out)