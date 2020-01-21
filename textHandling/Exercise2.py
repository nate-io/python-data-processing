# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 12:05:54 2020

@author: nate
"""

import os
import pandas

TARGET_DIR="D:\\python-course-files\\section-4-exercises"
TARGET_FILE = "IncomeByStateClean.csv"
OUTPUT_FILE_NAME = "IncomeByStateCleanIntlMoney.csv"
EURO_CONVERSION_RATE = 0.9
POUNDS_CONVERSION_RATE = 0.77

def exercise2():
    os.chdir(TARGET_DIR)
    
    # read file in as dataframe
    dataframe = pandas.read_csv(TARGET_FILE)
    
    # data manipulation
    dataframe["EUROS"] = dataframe["1984"] * EURO_CONVERSION_RATE
    dataframe["POUNDS"] = dataframe["1984"] * POUNDS_CONVERSION_RATE
    
    # export specifying not to add index label column
    dataframe.to_csv(OUTPUT_FILE_NAME,index=0)