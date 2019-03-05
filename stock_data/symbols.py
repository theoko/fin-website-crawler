import ftplib
import os
import re

class Symbol:

    def __init__(self):
        # Connect to ftp.nasdaqtrader.com
        self.ftp = ftplib.FTP('ftp.nasdaqtrader.com', 'anonymous', 'anonymous@debian.org')
        self.files = ["nasdaqlisted.txt", "otherlisted.txt"]

    def download(self):
        # Download files nasdaqlisted.txt and otherlisted.txt from ftp.nasdaqtrader.com
        for ficheiro in self.files:
                self.ftp.cwd("/SymbolDirectory")
                localfile = open(ficheiro, 'wb')
                self.ftp.retrbinary('RETR ' + ficheiro, localfile.write)
                localfile.close()
        self.ftp.quit()

    def write_file(self):
        # Grep for common stock in nasdaqlisted.txt and otherlisted.txt
        for ficheiro in self.files:
                localfile = open(ficheiro, 'r')
                for line in localfile:
                        if re.search("Common Stock", line):
                                ticker = line.split("|")[0]
                                # Append tickers to file tickers.txt
                                open("tickers.txt","a+").write(ticker + "\n")

    def tickers_file_exists(self):
        return os.path.isfile("tickers.txt")

    def get_ticker_list(self):
        if self.tickers_file_exists():
            with open("tickers.txt") as f:
                tickers = f.readlines()

            # Remove new line
            tickers = [x.strip() for x in tickers]

            return tickers
        else:
            return []

    """
    Get company name by ticker
    """
    def get_company_name(self, ticker):
        companies = []

        # Open files and return company name 
        for f in self.files:
            with open(f) as 
        
        # Remove new line
        # companies = [x.strip() for x in tickers]
