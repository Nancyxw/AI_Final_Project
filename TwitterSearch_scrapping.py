# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 12:54:30 2017

@author: maximjxw
"""

import json
import pymongo
import tweepy

with open('consumer_key.txt', 'r') as f:
    consumer_key =  f.read()
f.closed

with open('consumer_secret.txt', 'r') as f:
    consumer_secret = f.read()
f.closed

with open('access_key.txt', 'r') as f:
    access_key = f.read()
f.closed

with open('access_secret.txt', 'r') as f:
     access_secret = f.read()
f.closed

#Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

print("success!")

#connect to mongoDB
try:
    #use your database name, user and password here:
    #mongodb://<dbuser>:<dbpassword>@<mlab_url>/<database_name>
    with open("credentials.txt", 'r', encoding='utf-8') as f:
        [name,password,url,dbname]=f.read().splitlines()
        conn=pymongo.MongoClient("mongodb://{}:{}@{}/{}".format(name,password,url,dbname))
        print ("Connected successfully!!!")
except pymongo.errors.ConnectionFailure as e:
    print ("Could not connect to MongoDB: %s" % e) 

db = conn['aifinalproject']
collection = db['MSAI_test5_3pm']

#Using TwitterSearch (https://github.com/ckoepp/TwitterSearch)
from TwitterSearch import *
try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(['MicrosoftAI']) # let's define all words we would like to have a look for
    tso.set_language('en') # we want to see English tweets only
    tso.set_include_entities(False) # and don't give us all those entity information

    # it's about time to create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
        consumer_key = consumer_key,
        consumer_secret = consumer_secret,
        access_token = access_key,
        access_token_secret = access_secret
     )

     # this is where the fun actually starts :)
    data = []
    for tweet in ts.search_tweets_iterable(tso):
        data.append(tweet)
#        print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )

except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)

#Convert to csv (optional)
import pandas as pd
df = pd.DataFrame(data)
df.to_csv("MSAI_test5.csv")