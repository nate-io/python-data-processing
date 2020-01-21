# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 13:51:48 2020

@author: nate

Concat all files horizontally
"""

import os
import glob
import pandas

INPUT_DIR = 'D:\python-course-files\exercises-output\income30years'
OUTPUT_DIR = 'D:\python-course-files\exercises-output\income30years'
OUTPUT_FILE = 'IncomeByStateByYear.csv'

def concatenateHorizontal(indir = INPUT_DIR, outdir = OUTPUT_DIR):
    os.chdir(indir)
    
    # output safety check
    if not os.path.exists(outdir):
        os.makedirs(outdir)
        
    fileList = glob.glob("*.xls")
    
    # list of dataframes
    dfList = []

    # read data in & place in list    
    for filename in fileList:
        print(filename)
        
        df = pandas.read_excel(filename, header=None, skiprows=3)
        dfList.append(df)
        
    # manipulate data & write new output 
    # file concat'd horizontally (axis=1 == axis='column')
    concatedDf = pandas.concat(dfList, axis=1)
    concatedDf.to_csv(OUTPUT_FILE, index=None, header=None)
