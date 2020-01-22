# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 11:39:16 2020

@author: nate

All utility functions for processing pipeline
"""

import os
from ftplib import FTP, error_perm
import glob 
import patoolib
import pandas
import numpy
import matplotlib.pyplot as plt
import simplekml

DATA_DIR = "D:\\python-course-files"
OUT_DIR = os.path.join(DATA_DIR, "extracted")
COLUMN_NAMES = ["Year","Month","Day","Hour","Temp","DewTemp","Pressure","WindDir","WindSpeed", "Sky","Precip1","Precip6","ID"]
RAW_OUTPUT_FILE = 'Concatenated.csv'
LEFT_FILE = os.path.join(OUT_DIR, "Concatenated.csv")
RIGHT_FILE = os.path.join(OUT_DIR, "station-info.txt")
OUTPUT_FILE = os.path.join(OUT_DIR, "Concatenated-Merged.csv")
INFILE = os.path.join(OUT_DIR, "Concatenated-Merged.csv")
OUTFILE = os.path.join(OUT_DIR, "Pivoted.csv")
OUTPLOT = os.path.join(OUT_DIR, "plot-image.png")
KML_INPUT = os.path.join(OUT_DIR, "Pivoted.csv")
KML_OUTPUT = os.path.join(OUT_DIR, "Weather.kml")

# download files from course ftp server
def ftpDownloader(stationId, startYear, endYear, url='ftp.pyclass.com', user='student@pyclass.com', passwd='student123'):
    ftp = FTP(url)
    ftp.login(user, passwd)
    
    # nav to local dir safety
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    os.chdir(DATA_DIR)
    
    for year in range(startYear, endYear+1):
        """
        FTP data dir strcture is /Data/Year/StationId-Year.gz
        """
        fullpath = '/Data/%s/%s-%s.gz' % (year, stationId, year)
        filename = os.path.basename(fullpath)
        
        try:
            # retrieve file & store locally
            with open(filename,'wb') as file:
                ftp.retrbinary('RETR %s' % fullpath, file.write)
            print('%s successfully downloaded' % filename)
        except error_perm:
            # error_perm only handles errors in the 500 response code range
            # ftplib.all_errors would handle all regardless of code
            print('%s is not available' % filename)
            # remove locally created placeholder file
            os.remove(filename) 
    
    # cleanup
    ftp.close()

# extract files from archive formats
def extractFiles(indir = DATA_DIR, outdir = OUT_DIR):
    # head to input dir
    os.chdir(indir)
    
    # grab list of all files matching glob
    archives = glob.glob("*.gz")
    
    # output safety check
    if not os.path.exists(outdir):
        os.makedirs(outdir)
        
    # list existing files to prevent duplicate work
    files = os.listdir(outdir)
    
    for archive in archives:
        # data file contents match archive name minus the extension
        # remove from string and check
        if archive[:-3] not in files:
            patoolib.extract_archive(archive, outdir=outdir)
      
# adds the station name as a new field to extracted files
def addStationField(indir="D:\\python-course-files\\extracted"):
    # go to dir
    os.chdir(indir)
    
    # grab list of all files
    filenames = glob.glob('*')
    
    # add the station name as a new column for each file
    for filename in filenames:
        # read file in, no header, space delimited
        df = pandas.read_csv(filename, sep='\s+', header=None, error_bad_lines=False)
        # add the column name (derived from file name)
        # df.shape returns tuple specifying data dimensions
        # df.shape[0] is the number of rows in file, so write that many times
        df['Station'] = [filename.rsplit('-',1)[0]] * df.shape[0]
        # redirect to new file with no header/index
        df.to_csv(filename + '.csv', header=None, index=None)
        print(filename, df.shape)  

# concat all files into one large file
def concatenate(indir = OUT_DIR, outdir = OUT_DIR):
    os.chdir(indir)
        
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
    concatedDf.to_csv(RAW_OUTPUT_FILE, index=None)      

# augment station data with data from another file
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
    

# aggregate data intp pivot table for analysis
def pivot(infile = INFILE, outfile = OUTFILE):
    # named labels for column data we want output to pivot table
    pivotTableIndexes = ["ID", "LON", "LAT", "STATION NAME"]
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
    table = pandas.pivot_table(df, index=pivotTableIndexes, columns="Year", values = "Temp")
    table.to_csv(OUTFILE)
    
    # also return data for further processing
    return table

# output data plot as a bar graph for each weather station
def plot(outfigure = OUTPLOT):
    df = pivot()
    df.T.plot(subplots = True, kind = "bar")
    plt.savefig(outfigure, dpi = 200)
    
# build a kml file from data file
def kml(infile = KML_INPUT, outfile = KML_OUTPUT):
    # init simplekml instance
    kml = simplekml.Kml()
    
    df = pandas.read_csv(infile, index_col=["ID", "LON", "LAT", "STATION NAME"])
    
    # iterate over multiple rows dimensions of data using built-in zip function
    for lon, lat, name in zip(df.index.get_level_values("LON"), df.index.get_level_values("LAT"), df.index.get_level_values("STATION NAME")):
        # create kml point
        kml.newpoint(name = name, coords=[(lon, lat)])
        kml.save(outfile)
        
# helper method to run all utilities when script run as main
def runAll():
    stationIdsString = input('Enter station names divided by commas: ')
    startingYear = int(input('Enter the starting year of data to process: '))
    endingYear = int(input('Enter the ending year of data to process: '))
    stationIdList = stationIdsString.split(',')

    for station in stationIdList:
        ftpDownloader(station, startingYear, endingYear)

    extractFiles()
    addStationField()
    concatenate()
    merge()
    pivot()
    kml()
    plot()

# module system to expose functionality
if __name__ == "__main__":
  print('running main script ')
  runAll()