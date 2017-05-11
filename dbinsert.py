#!/home/sgrosu/anaconda2/bin/python
"""
Complete the insert_data function to insert the data into MongoDB.
"""

import json

def insert_data(data, db):
	db.arachnid.insert(data)



if __name__ == "__main__":
    
    from pymongo import MongoClient
    import urllib
    password = urllib.quote_plus('P@ssw0rd')
    client = MongoClient('mongodb://admin:'+password+'@127.0.0.1')
    db = client.examples

    with open('arachnid.json') as f:
        data = json.loads(f.read())
        insert_data(data, db)
        print db.arachnid.find_one()