# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 10:20:25 2020

@author: nate
"""

import os
import pandas
import numpy

INPUT_DIR = "D:\python-course-files\extracted"
INFILE = os.path.join(INPUT_DIR, "Concatenated-Merged.csv")
OUTFILE = os.path.join(INPUT_DIR, "Pivoted.csv")

# aggregate data for analysis
def pivot(infile = INFILE, outfile = OUTFILE):
    df = pandas.read_csv(infile)
    
    """
    data massage
        - data provider annotates null dtaa with -9999, replace with NaN
        - temp data is stored as value * 10 in order to not use floats, reconvert
    """
    df = df.replace(-9999, numpy.nan)
    df["Temp"] = df["Temp"]/10.0
    
    """
    aggregate data
        - aggregating the ID (weather station)
        - new columns are each year of data
        - values filling the columns are the Temp column values
    """
    table = pandas.pivot_table(df, index=["ID"], columns="Year", values = "Temp")
    table.to_csv(OUTFILE)
    