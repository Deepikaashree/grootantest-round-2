import tweepy as tw
import jsonpickle
consumer_key="I2y8ybmXPM8IBXGZ7f5oJJtzo"
consumer_secret="lbnnO7pQ9lhcgFCH6WmWbUPrWgVhJszhp4L5VnTmjzLSz9c0Wp"
access_token="1318474826613321728-ahR1su2V6W7grmGns1ohlyo9qvHGTE"
access_token_secret="8GLn9lk28ITVg6QTOrK1KwbFM8YyB6TPFRcqpKxT5j5Xb"
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tw.API(auth)

search_words = "corona"
date_since = "2020-10-16"
date_until = "2020-10-20"
tweet_count = 0
# Collect tweets
tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",since=date_since,
              until=date_until,result_type="popular").items(100)

fName = 'tweetExtract.txt' # where i save the tweets
with open(fName,'w') as f:
    # write all the new_tweets to a json file
    for tweet in tweets:
        print(tweet.retweet_count)
        f.write(jsonpickle.encode(tweet._json,unpicklable=False)+'\n')
        tweet_count+=1
        print("Successfully downloaded {0} tweets".format(tweet_count))