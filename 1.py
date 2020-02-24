import tweepy
consumer_key="S1csKsxU9JERbar9WjICktghe"
consumer_secret="cNUNfUkXR7QDIJirV2E8SgNWMUxxq7bmKUi7mbUN7HLlxLVDrO"
access_token="1009663549960941568-lPFTCj3s8pKcD331uHNjzghfz3OIYa"
access_token_secret="vLMN6B8vuA3lNM6KsM8Wtvy1lMUa4kggNqbNKTNsOOYJA"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

user = api.get_user("GameOfThrones")
print(user.name)
