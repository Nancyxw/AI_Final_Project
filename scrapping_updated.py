#Nancy - AI Final Project - Scrapping
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

#Start scarpping - #MicrosoftAI
from tweepy import Stream,StreamListener

class listener(StreamListener):
    def __init__(self):
        super(StreamListener, self).__init__()
        self.num_tweets = 0
        try:
            #use your database name, user and password here:
            #mongodb://<dbuser>:<dbpassword>@<mlab_url>/<database_name>
            with open("credentials.txt", 'r', encoding='utf-8') as f:
                [name,password,url,dbname]=f.read().splitlines()
                self.conn=pymongo.MongoClient("mongodb://{}:{}@{}/{}".format(name,password,url,dbname))
            print ("Connected successfully!!!")
        except pymongo.errors.ConnectionFailure as e:
            print ("Could not connect to MongoDB: %s" % e)
        self.db = self.conn['aifinalproject']
        self.collection = self.db['MicrosoftAI']

    def on_data(self, status):
        if self.num_tweets < 2000:
            json_data=json.loads(status)
            self.collection.insert_one(json_data)
            print (str('** '+json_data["user"]["screen_name"])+' ** : ' + json_data["text"])
            self.num_tweets += 1
            return True
        else:
            return False

    def on_error(self, status):
        print (status)

# Catch all tweets in Barcelona area and print them
twitterStream = Stream(auth, listener())
twitterStream.filter(track = ["#MicrosoftAI"])
print ("done")
