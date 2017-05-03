#!/home/sgrosu/anaconda2/bin/python

'''
Find the time and value of max load for each of the regions
COAST, EAST, FAR_WEST, NORTH, NORTH_C, SOUTHERN, SOUTH_C, WEST
and write the result out in a csv file, using pipe character | as the delimiter.

An example output can be seen in the "example.csv" file.
'''

import xlrd
import os
import csv
from zipfile import ZipFile

datafile = "2013_ERCOT_Hourly_Load_Data.xls"
outfile = "2013_Max_Loads.csv"


def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
    #data = None

    data = [['Station','Year','Month','Day','Hour','Max Load']]
    maxvalue = 0
    for i in range(1,9):
    	maxvalue = max(sheet.col_values(i,i,sheet.nrows))
    	#print maxvalue
    	rez = 0
    	for j in range(1,sheet.nrows):
    		if sheet.cell(j,i).value == maxvalue:
    			rez = j
    		else:
    			continue
	   	#print rez
	 	maxtime = sheet.cell(rez,0).value
	 	xl_maxtime = xlrd.xldate_as_tuple(maxtime,0)
	 	#print xl_maxtime[:4]
	 	a,b,c,d = xl_maxtime[:4]
	 	data.append([str(sheet.cell(0,i).value),a,b,c,d,maxvalue])
    # YOUR CODE HERE
    # Remember that you can use xlrd.xldate_as_tuple(sometime, 0) to convert
    # Excel date to Python tuple of (year, month, day, hour, minute, second)
    return data
 
def save_file(data, filename):
    # YOUR CODE HERE
    with open(filename,'wb') as ofile:
    	writer = csv.writer(ofile,delimiter='|')
    	#writer.writerow([str('Station|Year|Month|Day|Hour|Max Load')])
    	for elem in data:
    		writer.writerow(elem)




'''  
def test():
    open_zip(datafile)
    data = parse_file(datafile)
    save_file(data, outfile)

    number_of_rows = 0
    stations = []

    ans = {'FAR_WEST': {'Max Load': '2281.2722140000024',
                        'Year': '2013',
                        'Month': '6',
                        'Day': '26',
                        'Hour': '17'}}
    correct_stations = ['COAST', 'EAST', 'FAR_WEST', 'NORTH',
                        'NORTH_C', 'SOUTHERN', 'SOUTH_C', 'WEST']
    fields = ['Year', 'Month', 'Day', 'Hour', 'Max Load']

    with open(outfile) as of:
        csvfile = csv.DictReader(of, delimiter="|")
        for line in csvfile:
            station = line['Station']
            if station == 'FAR_WEST':
                for field in fields:
                    # Check if 'Max Load' is within .1 of answer
                    if field == 'Max Load':
                        max_answer = round(float(ans[station][field]), 1)
                        max_line = round(float(line[field]), 1)
                        assert max_answer == max_line

                    # Otherwise check for equality
                    else:
                        assert ans[station][field] == line[field]

            number_of_rows += 1
            stations.append(station)

        # Output should be 8 lines not including header
        assert number_of_rows == 8

        # Check Station Names
        assert set(stations) == set(correct_stations)

        
if __name__ == "__main__":
    test()
'''
save_file(parse_file(datafile),outfile)