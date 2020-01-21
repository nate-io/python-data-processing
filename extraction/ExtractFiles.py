# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 07:12:48 2020

@author: nate
"""

import os
import glob 
import patoolib

IN_DIR = "D:\python-course-files"
OUT_DIR = os.path.join(IN_DIR, "extracted")

def extractFiles(indir = IN_DIR, outdir = OUT_DIR):
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