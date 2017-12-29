# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 18:25:30 2017

@author: maximjxw
"""

for tweet in tweepy.Cursor(api.search,q="BREXIT -filter:retweets",count=200,
                           lang="en",
                           since="2017-12-11",
                           until="2017-12-13",
                          geodata="52,-1,500km",
                           tweet_mode="extended"
                          ).items():
    print (tweet.created_at, tweet.full_text, tweet.user.id, "Retweets",tweet.retweet_count, "Favorites",tweet.favorite_count)

csvWriter.writerow([tweet.created_at, tweet.full_text, tweet.user.id,tweet.retweet_count,tweet.favorite_count])