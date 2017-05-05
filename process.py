#!/home/sgrosu/anaconda2/bin/python
# -*- coding: utf-8 -*-
"""
Let's assume that you combined the code from the previous 2 exercises with code
from the lesson on how to build requests, and downloaded all the data locally.
The files are in a directory "data", named after the carrier and airport:
"{}-{}.html".format(carrier, airport), for example "FL-ATL.html".

The table with flight info has a table class="dataTDRight". Your task is to
use 'process_file()' to extract the flight data from that table as a list of
dictionaries, each dictionary containing relevant data from the file and table
row. This is an example of the data structure you should return:

data = [{"courier": "FL",
         "airport": "ATL",
         "year": 2012,
         "month": 12,
         "flights": {"domestic": 100,
                     "international": 100}
        },
         {"courier": "..."}
]

Note - year, month, and the flight data should be integers.
You should skip the rows that contain the TOTAL data for a year.

There are couple of helper functions to deal with the data files.
Please do not change them for grading purposes.
All your changes should be in the 'process_file()' function.

The 'data/FL-ATL.html' file in the tab above is only a part of the full data,
covering data through 2003. The test() code will be run on the full table, but
the given file should provide an example of what you will get.
"""
from bs4 import BeautifulSoup
from zipfile import ZipFile
import os

datadir = "."


def open_zip(datadir):
    with ZipFile('{0}.zip'.format(datadir), 'r') as myzip:
        myzip.extractall()


def process_all(datadir):
    files = os.listdir(datadir)
    return files


def process_file(f):
    """
    This function extracts data from the file given as the function argument in
    a list of dictionaries. This is example of the data structure you should
    return:

    data = [{"courier": "FL",
             "airport": "ATL",
             "year": 2012,
             "month": 12,
             "flights": {"domestic": 100,
                         "international": 100}
            },
            {"courier": "..."}
    ]


    Note - year, month, and the flight data should be integers.
    You should skip the rows that contain the TOTAL data for a year.
    """
    data = []
    
    # Note: create a new dictionary for each entry in the output data list.
    # If you use the info dictionary defined here each element in the list 
    # will be a reference to the same info dictionary.
    with open("{}/{}".format(datadir, f), "r") as html:

        soup = BeautifulSoup(html,'lxml')

    numbers = soup.find(id="DataGrid1")
    a = numbers.find_all("tr", class_="dataTDRight")
    #print a, len(a)
    l = []
    for element in a:
        subl = []
        for el in element.find_all('td'):
            subl.append(el.contents)
        s = [item for sublist in subl for item in sublist]
        l.append(s)
    #print l

    
    for elem in l:
        if 'TOTAL' in elem[1]:
                continue
        else:
            info = {}
            info["courier"], info["airport"] = f[:6].split("-")
            info["flights"] = {"domestic":0,"international":0}
            for i in range(4):
                
                #print int(elem[i].encode('utf-8').replace(',',''))
                if i == 0:
                    info["year"] = int(elem[i].encode('utf-8').replace(',',''))
                if i == 1:
                    info["month"] = int(elem[i].encode('utf-8').replace(',',''))
                if i == 2:
                    info["flights"]["domestic"] = int(elem[i].encode('utf-8').replace(',',''))
                if i == 3:
                    info["flights"]["international"] = int(elem[i].encode('utf-8').replace(',',''))
            #print info["flights"]["domestic"]
            data.append(info)
    
    return data

'''
def test():
    print "Running a simple test..."
    open_zip(datadir)
    files = process_all(datadir)
    data = []
    # Test will loop over three data files.
    for f in files:
        data += process_file(f)
        
    assert len(data) == 399  # Total number of rows
    for entry in data[:3]:
        assert type(entry["year"]) == int
        assert type(entry["month"]) == int
        assert type(entry["flights"]["domestic"]) == int
        assert len(entry["airport"]) == 3
        assert len(entry["courier"]) == 2
    assert data[0]["courier"] == 'FL'
    assert data[0]["month"] == 10
    assert data[-1]["airport"] == "ATL"
    assert data[-1]["flights"] == {'international': 108289, 'domestic': 701425}
    
    print "... success!"

if __name__ == "__main__":
    test()

'''

print process_file("FL-ATL.html")