#!/home/sgrosu/anaconda2/bin/python
"""
Your task is to check the "productionStartYear" of the DBPedia autos datafile for valid values.
The following things should be done:
- check if the field "productionStartYear" contains a year
- check if the year is in range 1886-2014
- convert the value of the field to be just a year (not full datetime)
- the rest of the fields and values should stay the same
- if the value of the field is a valid year in the range as described above,
  write that line to the output_good file
- if the value of the field is not a valid year as described above, 
  write that line to the output_bad file
- discard rows (neither write to good nor bad) if the URI is not from dbpedia.org
- you should use the provided way of reading and writing data (DictReader and DictWriter)
  They will take care of dealing with the header.

You can write helper functions for checking the data and writing the files, but we will call only the 
'process_file' with 3 arguments (inputfile, output_good, output_bad).
"""
import csv
import pprint
import re

INPUT_FILE = 'autos.csv'
OUTPUT_GOOD = 'autos-valid.csv'
OUTPUT_BAD = 'FIXME-autos.csv'

def process_file(input_file, output_good, output_bad):

    with open(input_file, "r") as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames
        #read = list(reader)
        #COMPLETE THIS FUNCTION
        goodlist = []
        badlist = []
        horlist = []
        for row in reader:
            #print row["productionStartYear"]
            try:
                year = re.findall("(\d\d\d\d)[\-]",row["productionStartYear"])[0]
                #print year
                if 'dbpedia.org' in row["URI"]:

                    if 1886 <= int(year) and int(year) <= 2014:                   
                        row["productionStartYear"] = int(year)
                        goodlist.append(row)
                    else:
                        badlist.append(row)
                else:
                    horlist.append(row)
            except:
                #print row["productionStartYear"]
                if 'dbpedia.org' in row["URI"]:
                    badlist.append(row)
                else:
                    horlist.append(row)




    
    # This is just an example on how you can use csv.DictWriter
    # Remember that you have to output 2 files
    with open(OUTPUT_GOOD, "w") as g:
        writer = csv.DictWriter(g, delimiter=",", fieldnames= header)
        writer.writeheader()
        for row in goodlist:
            writer.writerow(row)

    with open(OUTPUT_BAD, "w") as b:
        writer = csv.DictWriter(b, delimiter=",", fieldnames= header)
        writer.writeheader()
        for row in badlist:
            writer.writerow(row)

    with open('horror.csv', "w") as h:
        writer = csv.DictWriter(h, delimiter=",", fieldnames= header)
        writer.writeheader()
        for row in horlist:
            writer.writerow(row)
    
    #return badlist

    

'''
def test():

    process_file(INPUT_FILE, OUTPUT_GOOD, OUTPUT_BAD)


if __name__ == "__main__":
    test()
'''

process_file(INPUT_FILE,OUTPUT_GOOD,OUTPUT_BAD)