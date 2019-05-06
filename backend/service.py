import tweepy
from deprazer.reader import read_corpus
from deprazer.wrappers import Deprazer

model = Deprazer.load('model')
depression_treshold = 0.5

def get_tweets_by_account_and_time(twitter_account, from_date):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    api = tweepy.API(auth)

    for tweet in api.user_timeline(screen_name=twitter_account, count=1):
        print(tweet)

    return []

def get_tweets_by_location(area_name, from_date):
    # todo: use twitter API or alternatives
    return []

def get_user_depression_level(twitter_account, from_date):
    tweets = get_tweets_by_account_and_time(twitter_account, from_date)
    return get_tweets_depression_level(tweets)

def get_verbose_area_depression_level(area_name, from_date):
    result = get_area_depression_level(area_name, from_date)
    depression_level = get_area_depression_level(area_name, from_date)

    return {"state": area_name, "depression": depression_level["value"] / depression_level["total"], "keywords": depression_level["keywords"]}

def get_area_depression_level(area_name, from_date):
    tweets = get_tweets_by_location(area_name)
    return get_tweets_depression_level(tweets)

def get_tweets_depression_level(tweets):
    # todo: get real tweets
    # corpus = tweets
    corpus = ['so stressed', 'i feel bad']
    result = model.predict_corpus(corpus)

    # todo: get keywords correctly
    keywords = ""
    return { "value": result, "keywords": keywords }
