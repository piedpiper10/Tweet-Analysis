import tweepy
import datetime
import xlsxwriter
import sys
consumerKey="S1csKsxU9JERbar9WjICktghe"
consumerSecret="cNUNfUkXR7QDIJirV2E8SgNWMUxxq7bmKUi7mbUN7HLlxLVDrO"
accessToken="1009663549960941568-lPFTCj3s8pKcD331uHNjzghfz3OIYa"
accessTokenSecret="vLMN6B8vuA3lNM6KsM8Wtvy1lMUa4kggNqbNKTNsOOYJA"

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
username="GameOfThrones"
api = tweepy.API(auth)

startDate = datetime.datetime(2017, 6,1, 0, 0, 0)
endDate =   datetime.datetime(2017, 8, 31, 23, 23, 23)
hashtags_dict = {}
tweets = []
tmpTweets = api.user_timeline(username)
for tweet in tmpTweets:
    if tweet.created_at < endDate and tweet.created_at > startDate:
        tweets.append(tweet)

while (tmpTweets[-1].created_at > startDate):
    print("Last Tweet @", tmpTweets[-1].created_at, " - fetching some more")
    tmpTweets = api.user_timeline(username, max_id = tmpTweets[-1].id)
    for tweet in tmpTweets:
        if tweet.created_at < endDate and tweet.created_at > startDate:
            tweets.append(tweet)

workbook = xlsxwriter.Workbook("GameofThrones1.xlsx")
worksheet = workbook.add_worksheet()
row = 0
for tweet in tweets:
        hashtags = tweet.entities.get('hashtags')
        for hashtag in hashtags:
            if hashtag['text'] in hashtags_dict.keys():
                hashtags_dict[hashtag['text']] += 1
            else:
                hashtags_dict[hashtag['text']] = 1

print(sorted(hashtags_dict, key=hashtags_dict.get, reverse=True)[:10])
'''
for tweet in tweets:
    worksheet.write_string(row, 0, str(tweet.id))
    worksheet.write_string(row, 1, str(tweet.created_at))
    worksheet.write(row, 2, tweet.text)
    worksheet.write_string(row, 3, str(tweet.in_reply_to_status_id))
    worksheet.write(row, 4, tweet.retweet_count)
    row += 1
'''
workbook.close()
print("Excel file ready")
