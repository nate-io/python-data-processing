# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 12:38:22 2020

@author: nate
"""

import os
import pandas

TARGET_DIR="D:\\python-course-files\\section-4-exercise"
TARGET_FILE = "Income-By-State-1984.xls"
OUTPUT_FILE_NAME = "IncomeByStateClean.csv"

def exercise1():
    os.chdir(TARGET_DIR)
    
    # read file in as dataframe, removing three top junk haders
    dataframe = pandas.read_excel(TARGET_FILE, skiprows=3)
    
    # export specifying not to add index label column
    dataframe.to_csv(OUTPUT_FILE_NAME,index=0)