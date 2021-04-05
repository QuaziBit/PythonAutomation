# PythonAutomation
Automation of web browsers for stock trading

# Project structure
## 1: download directory
Download: the CSV files will be download into this directory and after combining all CSV files
into the one this directory will be cleared.
## 2: drivers directory
Drivers: here we have drivers for Chrome web-browser and for FireFox web-browser.
Currently Chrome web-browser is not included and is not used.
## 3: output directory
Output: here we have all-ascending.csv, all-descending.csv, and all-no-sorting.csv files.
These files are CSV files and they should store final and combined data from the downloaded CSV files.
Before combining downloaded CSV files and create new data report these files will be cleared.
## 4: view directory
View: here we have a basic index.html and CSS files.
After running this application you need to copy the final generated html content from the output.html into the index.html.

# output.html
Output.html file: here are stored retrieved stock graphs as partial table.

# What must be installed
1: Python 3.8.6 62-bit

# How to create virtual environment
1: > mkdir myproject \
2: > cd myproject \
3: > py -3 -m venv stocks_v1

# Python 3 packages must be installed
1: Navigate to stocks_v1 directory \
2: > .\Scripts\Activate.ps1 \
3: Install following packages: \
4: pip3 install selenium \
5: pip3 install requests \
6: pip3 install urllib3 \
7: pip3 install beautifulsoup4 \
8: pip3 install lxml

# How to run:
1: Navigate to stocks_v1 directory \
2: > .\Scripts\Activate.ps1 \
3: You can sort stocks data based on its price in ascending or descending order, or keep it unsorted. \
4: for ascending order > py .\run.py ascending \
5: for descending order > py .\run.py descending \
6: for unsorted order > py .\run.py or py .\run.py no-sorting

