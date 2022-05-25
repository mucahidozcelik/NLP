import snscrape.modules.twitter as sntwitter
import csv
import pandas as pd



maxTweets = 10000

csvFile = open('geziparkı_tweets.csv', 'a', newline='', encoding='utf8')


csvWriter = csv.writer(csvFile)
csvWriter.writerow(['text'])


for i,tweet in enumerate(sntwitter.TwitterSearchScraper('#geziparkı + since:2013-05-27 until:2013-07-02 lang:"tr"').get_items()):
        if i > maxTweets :
            break
        csvWriter.writerow([tweet.user.username,tweet.date,tweet.content,tweet.user.location,
                            tweet.likeCount,tweet.retweetCount,tweet.user.followersCount,tweet.url])
csvFile.close()

df = pd.read_csv('geziparkı_tweets.csv')
df.reset_index(inplace=True)

df.columns = ['username', 'date','tweet','location','like_count','retweet_count','followers_count','url']
df.head()
df.info
df.describe().T


