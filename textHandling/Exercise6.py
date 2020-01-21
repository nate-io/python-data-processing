# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 14:08:18 2020

@author: nate
"""
import os
import pandas
import seaborn as sns
import matplotlib.pyplot as plt

DATA_DIR = "D:\python-course-files\exercises-output\income"
INPUT = os.path.join(DATA_DIR, "IncomeByStateByYearUniqueWithState.csv")
OUTPUT = os.path.join(DATA_DIR, "IncomeHeatmap.png")

def generatePlot(infile = INPUT, outfile = OUTPUT):
    # read file
    df=pandas.read_csv(infile)
    df=df.set_index(['GEOID','State'])
    
    # set up chart plot
    # this subplots def. produces only one cartesian chart
    fig, axes = plt.subplots()
    
    # config
    axes.tick_params(labelsize=4)
    
    # generate a heatmap using our dataframe
    sns.heatmap(df, ax=axes)
    
    # output chart as image
    fig.savefig(outfile ,dpi=200)
    