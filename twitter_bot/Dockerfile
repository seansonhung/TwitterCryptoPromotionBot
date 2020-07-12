FROM python:3.7-alpine

COPY bots/config.py /bots/
COPY bots/auto_tweets.py /bots/
COPY bots/auto_retweet_fav.py /bots/
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /bots
CMD ["python3", "auto_tweets.py"] & ["python3", "auto_retweet_fav.py"]