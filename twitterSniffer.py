import tweepy as tw
#Import your keys Please


auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

userID = "realDonaldTrump"

tweets = api.user_timeline(screen_name=userID,count=200,include_rts = False,tweet_mode="extended")

all_tweets = []
all_tweets.extend(tweets)
oldest_id = tweets[-1].id
while True:
    tweets = api.user_timeline(screen_name=userID, 
                           # 200 is the maximum allowed count
                           count=200,
                           include_rts = False,
                           max_id = oldest_id - 1,
                           # Necessary to keep full_text 
                           # otherwise only the first 140 words are extracted
                           tweet_mode = 'extended'
                           )
    if len(tweets) == 0:
        break
    oldest_id = tweets[-1].id
    all_tweets.extend(tweets)
    print('N of tweets downloaded till now {}'.format(len(all_tweets)))

for info in all_tweets:     
     listOfTxt = info.full_text.split(" ")
     for i in listOfTxt:
         if "://" in i  :
             listOfTxt.remove(i)
        
     tweet= " ".join(listOfTxt)


with open("trumpTweets.txt", "w") as txtFile:
    for info in all_tweets:     
     listOfTxt = info.full_text.split(" ")
     for i in listOfTxt:
         if "://" in i  :
             listOfTxt.remove(i)
        
     tweet= " ".join(listOfTxt)
     txtFile.write(tweet + "\n")
