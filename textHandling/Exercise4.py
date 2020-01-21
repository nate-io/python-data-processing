# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 13:51:48 2020

@author: nate

Concat all files horizontally, removing duplicate columns
"""

import os
import pandas

ROOT = 'D:\python-course-files\exercises-output\income30years'
INPUT_FILE = os.path.join(ROOT, "IncomeByStateByYear.csv")
OUTPUT_FILE = os.path.join(ROOT, 'IncomeByStateByYearUnique.csv')

def deduplicate_columns(inFile = INPUT_FILE, outFile = OUTPUT_FILE):
    os.chdir(ROOT)
        
    df = pandas.read_csv(inFile)
    
    """
    Remove the duplicate columns
        - T stands for transpose, drop_duplicates operates on ROWS
        - so transpose to swap column names to row data, drop dupes & re-transpose
    """
    noDupeDf = df.T.drop_duplicates().T
    
    noDupeDf.to_csv(outFile, index=None)
