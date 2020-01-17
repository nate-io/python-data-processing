# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 06:51:13 2020

@author: nate

Function to extract contents from archives

Used patool lib, must `pip install patool`

rar files require special handling on Windows (ofc it does...)
  - must have program installed to handle rar
  - program must be added to system PATH
  - extract_archive accepts 3rd param listing program to use like so:
      patoolib.extract_archive(FILENAME, OUTDIR, program="unrar")
"""

import os, patoolib

def extractionIntro():
    ARCHIVE_DIR = "D:\\python-course-files"
    UNPACKED_DIR = "unpack"
    OUTPUT_DIR = os.path.join(ARCHIVE_DIR, UNPACKED_DIR)
    
    os.chdir(ARCHIVE_DIR)
    
    patoolib.extract_archive("File1.gz",outdir=OUTPUT_DIR)
    patoolib.extract_archive("File2.zip",outdir=OUTPUT_DIR)