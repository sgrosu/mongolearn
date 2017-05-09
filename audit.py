#!/home/sgrosu/anaconda2/bin/python
# -*- coding: utf-8 -*-
"""
In this problem set you work with cities infobox data, audit it, come up with a
cleaning idea and then clean it up. In the first exercise we want you to audit
the datatypes that can be found in some particular fields in the dataset.
The possible types of values can be:
- NoneType if the value is a string "NULL" or an empty string ""
- list, if the value starts with "{"
- int, if the value can be cast to int
- float, if the value can be cast to float, but CANNOT be cast to int.
   For example, '3.23e+07' should be considered a float because it can be cast
   as float but int('3.23e+07') will throw a ValueError
- 'str', for all other values

The audit_file function should return a dictionary containing fieldnames and a 
SET of the types that can be found in the field. e.g.
{"field1": set([type(float()), type(int()), type(str())]),
 "field2": set([type(str())]),
  ....
}
The type() function returns a type object describing the argument given to the 
function. You can also use examples of objects to create type objects, e.g.
type(1.1) for a float: see the test function below for examples.

Note that the first three rows (after the header row) in the cities.csv file
are not actual data points. The contents of these rows should note be included
when processing data types. Be sure to include functionality in your code to
skip over or detect these rows.
"""
import codecs
import csv
import json
import pprint

CITIES = 'cities.csv'

FIELDS = ["name", "timeZone_label", "utcOffset", "homepage", "governmentType_label",
          "isPartOf_label", "areaCode", "populationTotal", "elevation",
          "maximumElevation", "minimumElevation", "populationDensity",
          "wgs84_pos#lat", "wgs84_pos#long", "areaLand", "areaMetro", "areaUrban"]

def audit_file(filename, fields):
    fieldtypes = {}
    dat = []
    with open(filename, 'r') as fi:
      data = csv.DictReader(fi,delimiter=',')
      for i in range(1,4):
        next(data, None)

      header = data.fieldnames 
      #print list(data)[0]

      for field in fields:
        typeset = []
        for row in data:
          try:
            float(row[field])
            try:
              int(row[field])
              typeset.append(type(int()))
            except:
              typeset.append(type(float()))
          except:
            if row[field].startswith('{'):
              typeset.append(type([]))
            elif row[field] == '' or row[field] == 'NULL':
              typeset.append(type(None))
            else:
              typeset.append(type(str()))
        fi.seek(0)
        data.__init__(fi,delimiter=',')
        for i in range(1,4):
          next(data, None)
        header = data.fieldnames 
        fieldtypes[field] = set(typeset)

   
    # YOUR CODE HERE


    return fieldtypes


def test():
    fieldtypes = audit_file(CITIES, FIELDS)

    pprint.pprint(fieldtypes)

    assert fieldtypes["areaLand"] == set([type(1.1), type([]), type(None)])
    assert fieldtypes['areaMetro'] == set([type(1.1), type(None)])
    
if __name__ == "__main__":
    test()
'''

print audit_file(CITIES,FIELDS)
'''