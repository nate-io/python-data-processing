# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 13:11:10 2020

@author: nate

Concatenate list of weather station csv files
"""

import os
import glob
import pandas

INPUT_DIR = 'D:\python-course-files\output-test'
OUTPUT_DIR = 'D:\python-course-files\output-test'
COLUMN_NAMES = ["Year","Month","Day","Hour","Temp","DewTemp","Pressure","WindDir","WindSpeed",
                "Sky","Precip1","Precip6","ID"]
OUTPUT_FILE = 'Concatenated.csv'

def concatenate(indir = INPUT_DIR, outdir = OUTPUT_DIR):
    os.chdir(indir)
    
    # output safety check
    if not os.path.exists(outdir):
        os.makedirs(outdir)
        
    fileList = glob.glob("*.csv")
    
    # list of dataframes
    dfList = []

    # read data in & place in list    
    for filename in fileList:
        print(filename)
        
        df = pandas.read_csv(filename, header=None)
        dfList.append(df)
        
    # manipulate data & write new output file
    concatedDf = pandas.concat(dfList)
    concatedDf.columns = COLUMN_NAMES
    concatedDf.to_csv(OUTPUT_FILE, index=None)
    