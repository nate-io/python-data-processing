# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 11:11:41 2020

@author: nate

Manipulate a group of files by adding a column name
"""

import os
import glob
import pandas

def addField(indir='D:\python-course-files\output-test'):
    # go to dir
    os.chdir(indir)
    
    # grab list of all files
    filenames = glob.glob('*')
    
    # add the station name as a new column for each file
    for filename in filenames:
        # read file in, no header, space delimited
        df = pandas.read_csv(filename, sep='\s+', header=None)
        # add the column name (derived from file name)
        # df.shape returns tuple specifying data dimensions
        # df.shape[0] is the number of rows in file, so write that many times
        df['Station'] = [filename.rsplit('-',1)[0]] * df.shape[0]
        # redirect to new file with no header/index
        df.to_csv(filename + '.csv', header=None, index=None)
        print(filename, df.shape)
            