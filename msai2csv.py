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
dbCC = connCC.aifinalproject_1
collection = dbCC.Magic_Leap

#collect the data
Data = []
for i in collection.find():
    Data.append(i)

df = pd.DataFrame(Data)
df.to_csv('magicleap.csv',encoding = 'utf-8')
