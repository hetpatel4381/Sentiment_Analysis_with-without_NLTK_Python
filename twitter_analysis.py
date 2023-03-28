import GetOldTweets3 as got

def get_tweets():
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('corona virus')\
        .setSince("2019-05-01")\
        .setUntil("2020-02-28")\
        .setMaxTweets(10)
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    text_tweets = [[tweet.text] for tweet in tweets]
    print(text_tweets)

get_tweets()