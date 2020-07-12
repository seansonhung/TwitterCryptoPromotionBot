import tweepy
import logging
import time
from config import create_api

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def main():
  api = create_api()

  while(True):
    newest_tweet = api.user_timeline(screen_name='@cryptocom', count = 1, include_rts = False)[0]
    if newest_tweet.in_reply_to_status_id is not None:
      # ignore replies
      return
      # if not fav, fav
    if not newest_tweet.favorited:
      try:
          newest_tweet.favorite()
      except Exception as e:
          logger.error("Error on fav", exc_info=True)
    # if not retweet yet, retweet
    if not newest_tweet.retweeted:
      # Retweet, since we have not retweeted it yet
      try:
          newest_tweet.retweet()
      except Exception as e:
          logger.error("Error on fav and retweet", exc_info=True)
    #Check every hour
    time.sleep(3600)
if __name__ == "__main__":main()