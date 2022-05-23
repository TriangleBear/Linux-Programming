import requests
from keys import keys
import tweepy
import urllib.request, json
import shutil
import time

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']
CAT_KEY = keys['cat_api']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

bot_id = int(api.verify_credentials().id_str)
mention_id=1

baseurl = 'https://api.thecatapi.com/v1/images/search'
words = ["cat pics please", "cat please"]
message = "testing... here you go @{} <3"


while True:
    replied = []
    mentions = api.mentions_timeline(since_id=mention_id)
    for mention in mentions:
        print(f"{mention.author.screen_name} - {mention.text}")
        mention_id = mention_id
        if mention.in_reply_to_status_id not in replied and mention.in_reply_to_status_id is None and mention.author.id != bot_id:
            if True in [word in mention.text.lower() for word in words]:
                try:
                    
                    with urllib.request.urlopen(baseurl) as url:
                        data = json.loads(url.read().decode())
                        img = data[0]
                        image_url = img['url']

                    filename = image_url.split("/")[-1]
    
                    r = requests.get(image_url, stream =True)
    
                    if r.status_code == 200:
                        r.raw.decode_content = True
                        with open(filename,'wb') as f:
                            shutil.copyfileobj(r.raw,f)
                        print('Image sucessfully Downloaded: ',filename)
                    else:
                        print('Image Couldn\'t be retreived')
                        
                        
                    print("Attempting Reply...")
                    print(f"{mention.author.screen_name} - {mention.text}")
                    
                    
                    api.update_status_with_media(message.format(mention.author.screen_name), filename, in_reply_to_status_id=mention.id_str)
                    print("Reply Sent <3")
                    replied.append(mention.id)
                except Exception as exc:
                    print(exc)
        else:
            print('tweet already answerd')
            
    time.sleep(15)