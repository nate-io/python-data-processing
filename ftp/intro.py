# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 05:56:07 2020

@author: nate
"""
# ftp module
from ftplib import FTP

# establish connection
ftp = FTP("ftp.pyclass.com")
ftp.login("student@pyclass.com", "student123")

"""
nlst lists dir, param will list specified dir
does not nav to dir, just lists
"""
print(ftp.nlst())
print(ftp.nlst("Data"))

# navigation
ftp.cwd("Data")
ftp.cwd("..")

"""
best practice - close connections as ftp server
may throttle connection limit
"""
ftp.close()