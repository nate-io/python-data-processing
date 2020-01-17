# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 07:08:07 2020

@author: nate
"""
import os
from ftplib import FTP, error_perm

def ftpDownloader(stationId, startYear, endYear, url='ftp.pyclass.com', user='student@pyclass.com', passwd='student123'):
    LOCAL_TARGET_DIR = "D:\\python-course-files"
    ftp = FTP(url)
    ftp.login(user, passwd)
    
    # nav to local dir safety
    if not os.path.exists(LOCAL_TARGET_DIR):
        os.makedirs(LOCAL_TARGET_DIR)
    os.chdir(LOCAL_TARGET_DIR)
    
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
            
            
            
            
            