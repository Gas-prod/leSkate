import tweepy

def auth():

    consumer_key = "your_consumer_key"
    consumer_secret = "your_consumer_secret"

    access_token = "your_acces_token"
    access_token_secret = "your_access_token_secret"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    return api,auth


from tweepy.streaming import StreamListener
import time
import json

def contains_word(string, word):
    return (' ' + word + ' ') in (' ' + string + ' ')

class MyStreamListener(tweepy.StreamListener):

    def on_data(self, data):

        tweet = json.loads(data)
        id_tweet = tweet["id_str"]

        if not contains_word(tweet["text"][0], "@") and not tweet["is_quote_status"] and not tweet["text"].startswith("RT @"):
            api.retweet(id_tweet)
            print(tweet["text"])

api, auth = auth()

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener = myStreamListener)

myStream.filter(track = ["skateboard", "skate", "skateur", "skates", "skater", "kickflip", "heelflip", "shov it", "skatos", "skateshop", "@aurelgiraud_", "@Lask8boarderie", "@josephgarbaccio", "@redbullskate", "@biomeskateboard", "@rockslideshop", "@EDYNEclothing", "@vansskate"], languages=["fr"])
