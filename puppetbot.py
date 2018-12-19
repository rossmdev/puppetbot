# TWITTER BOT
# IMPORTS
import tweepy as tp 
import time
import os 

# KEYS
consumer_key = 'YOUR_CONSUMER_API_KEY'
consumer_secret = 'YOUR_CONSUMER_API_SECRET_KEY'
access_token = 'YOUR_ACCESS_TOKEN'
access_secret = 'YOUR ACCESS_SECRET_TOKEN'

# AUTH
auth  = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

# UPDATE WITH STATUS
os.chdir('puppet')
for puppet_image in os.listdir('.'):
    api.update_with_media(puppet_image, "Here's an update from puppetbot:")
    time.sleep(3600)