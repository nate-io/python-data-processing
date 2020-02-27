# -*- coding: utf-8 -*-
"""
Created on Thurs Feb 27 2020

@author: nate

Denormalize 5 years of stock data for project
"""

import os
import pandas

def concatStocks():
  stockInfoFile = 'stockInfo.csv'
  stock5YearsFile = 'stocks5Years.csv'
  mergedFile = 'denormalizedStocks.csv'

  stockInfoDf = pandas.read_csv(stockInfoFile)
  stockHistoryDf = pandas.read_csv(stock5YearsFile)

  mergedDf = pandas.merge(stockHistoryDf, stockInfoDf, on='Symbol')
  mergedDf.to_csv(mergedFile, index=0)