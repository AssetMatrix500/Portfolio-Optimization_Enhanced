# -*- coding: utf-8 -*-
"""
Author: Daniel Carpenter
Function To pull stock data

Financial Engineering
Final Project - July 2022
Modern Portfolio Theory - Portfolio Optimization
"""

import pandas   as pd
import yfinance as yf # Stock data -> pip install yfinance -> https://pypi.org/project/yfinance/


# =============================================================================
# Import stocks (monthly)
# =============================================================================


def pullStockData(StockTickers, minDate, maxDate, interval='1mo'):
    
    # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
    
    # Can dowload the following:
    # "Stock", "Open", "High", "Low", "Close", "Adj Close", "Volume"
    stockMetrics = ["Adj Close"]
    
    # Create df to hold the stocks pulled
    PulledStocks = pd.DataFrame(columns = stockMetrics)

    count = 0
    outOf = len(StockTickers)
    
    # Pull each stocks
    for stock in StockTickers:  
        
        count += 1 # Keep track
        
        # Get the stock ticker over the date range
        print('\nDownloading', stock, '- Progress:', count, '/', outOf)
        stockTicker = yf.download(stock, start=minDate, end=maxDate, 
                                  interval=interval)
        
        # Force reset to coerce to date
        stockTicker = stockTicker.reset_index()
        
        # Assign the ticker name to the stock
        stockTicker["Stock"] = stock
        
        # Concatenate the pulled stock history to the main data frame
        PulledStocks = pd.concat([PulledStocks, stockTicker])  
        
    # Final Column names for the stocks
    stockMetrics = ["Stock", "Date"] + stockMetrics
    PulledStocks = PulledStocks[stockMetrics] 
    
    # Rename the columns
    PulledStocks = PulledStocks.rename(columns = {'Stock':     'stock',
                                                  'Date':      'period',
                                                  'Adj Close': 'adjClose'})
    
    return PulledStocks.dropna() # drop na since mid month sometimes contains nan

