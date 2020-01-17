# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 06:13:18 2020

@author: nate
"""
from ftplib import FTP
import os


"""
    General purpose FTP downloader with default params
"""
def ftpDownloader(filename, host="ftp.pyclass.com", user="student@pyclass.com", passwd="student123"):
    LOCAL_TARGET_DIR = "D:\\python-course-files"
    ftp = FTP(host)
    ftp.login(user, passwd)
    
    # setup target dir on server
    ftp.cwd("Data")
    # nav to local dir safety
    if not os.path.exists(LOCAL_TARGET_DIR):
        os.makedirs(LOCAL_TARGET_DIR)
    os.chdir(LOCAL_TARGET_DIR)
    
    
    """
    Retrieving a file:
        process is to create a new file locally and download contents to it
        
        open - built in method to open a file
        as - handle to reference the open'd object
        with statement opens a new file with first param name
        wb specifies open for writing in binary format (since PDF)
        
        retrbinary == retrieve binary. RETR is the ftp command to retrieve and
        is required
        file.write is the callback exec'd for each chunk of data receieved
    """
    with open(filename,'wb') as file:
        ftp.retrbinary('RETR %s' %filename, file.write)