from deprazer.reader import read_corpus
from deprazer.wrappers import Deprazer

model = Deprazer.load('model')
depression_treshold = 0.5

def get_tweets_by_account_and_time(twitter_account, from_date):
    # todo: use twitter API or alternatives
    return []

def get_tweets_by_location(area_name, from_date):
    # todo: use twitter API or alternatives
    return []

def get_tweet_depression_confidence(tweets):
    # corpus = tweets
    corpus = ['so stressed']
    result = model.predict_corpus(corpus)
    print(result)
    return { "value": result, "keyword": "" }

def get_user_depression_level(twitter_account, from_date):
    tweets = get_tweets_by_account_and_time(twitter_account, from_date)
    return get_tweets_depression_level(tweets)

def get_verbose_area_depression_level(area_name, from_date):
    result = get_area_depression_level(area_name, from_date)
    depression_level = get_area_depression_level(area_name, from_date)

    return {"state": area_name, "depression": depression_level["depressed"] / depression_level["total"], "keywords": depression_level["keywords"]}

def get_area_depression_level(area_name, from_date):
    tweets = get_tweets_by_location(area_name)
    return get_tweets_depression_level(tweets)

def get_tweets_depression_level(tweets):
    total_depression = 0
    keywords_map = {}
    depression_confidence = get_tweet_depression_confidence(tweets)
    return { "depressed": depression_confidence["value"], "keywords": depression_confidence["keywords"] }

