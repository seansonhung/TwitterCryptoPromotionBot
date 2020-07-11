# tweepy-bots/bots/config.py
import tweepy
import logging

logger = logging.getLogger()

def create_api():
    ACCESS_KEY = "1281430365454970880-gZz0BRWZoc4ClcNBRNV44S9ttqLawM" 
    ACCESS_KEY_SECRET = "CHZcsq6OqBLWzWhkJkvsSlnRZmryxKAJQGOad5BM49DgP"
    API_KEY = "49QfMne8RK1KGkK0poOyf5UVO"
    API_KEY_SECRET = "YukQk0umfctkxYrbm3KCWa1Zxw79q3g6suFNWWml5ZiwzcLZsX"

    auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_KEY_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True, 
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api