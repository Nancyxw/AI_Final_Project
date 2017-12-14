# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 11:53:24 2017

@author: maximjxw
"""

import pymongo
import pandas as pd

try:
    #use your database name, user and password here:
    #mongodb://<dbuser>:<dbpassword>@<mlab_url>/<database_name>
    with open("credentials.txt", 'r', encoding='utf-8') as f:
        [name,password,url,dbname]=f.read().splitlines()
    connCC=pymongo.MongoClient("mongodb://{}:{}@{}/{}".format(name,password,url,dbname))
    print ("Connected successfully!!!")
    
except pymongo.errors.ConnectionFailure as e:
    print ("Could not connect to MongoDB: %s" % e) 

#test connection
connCC

#connect to the database
dbCC = connCC.aifinalproject
collection = dbCC.MicrosoftAI

#collect the data
Data = []
for i in collection.find():
    Data.append(i)

df = pd.DataFrame(Data)
df.to_csv('microsoftAI.csv')


#data analysis

"""
def read_mongo(db, collection, query={}, host='localhost', port=39436, username="nancyjiang", password="19931124", no_id=True):

    # Connect to MongoDB
    db = _connect_mongo(host=host, port=port, username=username, password=password, db=dbCC)

    # Make a query to the specific DB and Collection
    cursor = db[collection].find(query)

    # Expand the cursor and construct the DataFrame
    df =  pd.DataFrame(list(cursor))

    # Delete the _id
    if no_id:
        del df['_id']

    return df
"""