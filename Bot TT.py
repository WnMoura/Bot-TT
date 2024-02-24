import tweepy
import schedule

import time


api_key = "wETcURH9TaqCgsXsy9TSEchWn"
api_key_secret = "7Tk6vNgE1Hzk9XuUOjLRMULRUlWVxKcwZoH1048iryGgWa6Nzi"
bearer_token = r"AAAAAAAAAAAAAAAAAAAAAFVerQEAAAAAvn5lJbSAqRdNSpje2WuffcZ2lpU%3D9yi9KTVBdltLdkYGCYsK9HDEXv4CmG12n6PZY2r3hv60sFlzyy"
access_token = "1113228432257814530-z1aPqlEfzRQZXso7ktWqrupAyz53sv"
access_token_secret = "1qGqyUX34mGC9JDZDBgmbkS0Byn1MlJMUz2D17V3uPkNe"

client = tweepy.Client(bearer_token, api_key, api_key_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_key_secret, access_token, access_token_secret)
api = tweepy.API(auth)


def postar_tweet():
    tweet_texto = "Flu!" + str("!")
    client.create_tweet(text=tweet_texto)
    print("Tweet Postado com sucesso", tweet_texto)


schedule.every(10).seconds.do(postar_tweet)

while True:
    schedule.run_pending()
    time.sleep(1)
