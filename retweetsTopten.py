import tweepy as tw
consumer_key="I2y8ybmXPM8IBXGZ7f5oJJtzo"
consumer_secret="lbnnO7pQ9lhcgFCH6WmWbUPrWgVhJszhp4L5VnTmjzLSz9c0Wp"
access_token="1318474826613321728-ahR1su2V6W7grmGns1ohlyo9qvHGTE"
access_token_secret="8GLn9lk28ITVg6QTOrK1KwbFM8YyB6TPFRcqpKxT5j5Xb"
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tw.API(auth)
tweetcount = 1
search_words = "corona"
date_since = "2020-10-16"
date_until = "2020-10-20"
# Collect tweets
tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",since=date_since,
              until=date_until,result_type="popular").items(100)
tweetfin = {}
for tweet in tweets:
    tweetfin['tweet_'+str(tweetcount)]={'retweet_count':tweet.retweet_count,'screen_name':tweet.user.screen_name}
    #print(tweet.retweet_count,tweet.user.screen_name)
    tweetcount+=1
#print(tweetfin)
res = []
for x in tweetfin.values():
    res.append(x)
def myFunc(e):
    return e['retweet_count']
res.sort(key=myFunc,reverse=True)
print("First 10 tweets with retweet count and screen name:\n")
for x in range(0,10):
    print(res[x])
fName = 'retweets.json' # where i save the tweets
with open(fName,'w') as f:
    # write all the new_tweets to a json file
    for x in range(0,10):
        f.write(str(res[x])+'\n')