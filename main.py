import tweepy

def auth():

    consumer_key = "ASZOXEtX80SYUfvqIjmLH33AX"
    consumer_secret = "i0ZaUTEAnUh12ZfkMqYDXOcj0nc13YCuqGhqomcZ7gvVcF5sbA"

    access_token = "1373633196517117956-VvYUSl88XvwE5teeYcqXUFw6weXuGx"
    access_token_secret = "9GNI38ISXh0nn0PZeWEzDqO6I0yH2TYrwMbZFVi59x6hJ"

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

        if not contains_word(tweet["text"][0], "@") and not tweet["retweeted"] and not tweet["text"].startswith("RT @"):
            api.retweet(id_tweet)
            print(tweet["text"])

api, auth = auth()

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener = myStreamListener)

myStream.filter(track = ["skateboard", "skate", "skateur", "skates", "skater", "kickflip", "heelflip", "shov it", "skatos", "skateshop"], languages=["fr"])