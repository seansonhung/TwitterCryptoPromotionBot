import tweepy
import time
import random
from config import create_api

def main():
  api = create_api()

  saved_tweets = [
    "Patiently waiting for MCO card in Canada. \n Reserve and get $50 if you haven't",
    "How is your crypto profolio doing today? All I have is #CRO and #MCO.",
    "I made so many mistake when investing in crypto and still somehow made a bit of profit.",
    "I get wreck every time I tried to time the market lul. #CRO ",
    "Got $5 back after buying $50 PlayStation giftcard today.",
    "Is it weird to use gift card for everything? I literally buy gift cards before going shopping because 5-10 percent cash back.",
    "Love the syndicate but the oversubscription is insane @cryptocom #CRO #MCO",
    "I will gladly give my soul for 1 #BTC or MCO icy white card.",
    "I think I'm addicted to @cryptocom . Spent 5 minute staring at my daily earn of $.4 :)",
    "There's only ever 30 mil #MCO. Price will soar when there's more people with the MCO visa card.",
    "Got burned by #XRP when I first started investing. #MCO and #CRO is much safer. Even when price drop there are still so many incentive to HODL.",
    "Crypto token utility is almost here. I love MCO VISA card. 2 cash back on everything. Getting the green card soon for 3%.",
    "Just with free Netflix and Spotify alone I saved atleast $20 a month. Putting that money right back in #CRO for compound interest.",
    "@cryptocom Would be nice if the syndicate allocation is up to $1mil. The oversubscription is insane.",
    "@cryptocom should have big event for each mil users milestone. Keep the hype up! #CRO #MCO",
    "I only learned of #CRO through getting crypto.com card. It's already top 10 and there's still so many who don't know about it",
    "#CRO #MCO #BTC #ETH FIGHTING~~~~",
    "I'm the type of person to be giddy about a $1 daily interest earn #CRO",
    "Whatever money I get from cashback with @cryptocom card. I'm putting back into earn for compounding.",
    "I got into #CRO and #MCO kind of late but better late than never.",
    "Praying for #BTC today. Please be strong to pull up the alt childrens #CRO #MCO.",
    "Im hugging my @cryptocom card to sleep when it arrive in Canada.",
    "I put ~$100 back into #CRO #MCO per month by cash back on daily spending with the @cryptocom card",
    "When FOMO happen #CRO and #MCO will be insane because @cryptocom product is so good",
    "I will forever HODL my #CRO ",
    "Metal visa card is so badass. Why can't everyone be like @cryptocom",
    "My life will be complete when I get my hand on the Crypto.com icy white card.",
    "I will never regret investing in crypto. #BTC #CRO #MCO",
    "MCO visa card is best to increasing crypto utilization and exposure to the general public ",
    "Can't wait for COVID to end so I can go shopping with my @cryptocom card",
    "I wish I have a time machine to invest in #CRO sooner.",
    "My luck is so bad. The chance of winning a crypto giveaway is NIL",
    "@cryptocom Every week I look forward to syndicate even if my allocation is only $10 ;(",
    "bts and black pink got nothing on my @cryptocom #CRO",
    "I go to sleep happy after seeing my $.5 #CRO earn deposited",
    "First thing I do in the morning is pray to the universe for the crypto market. Then I opening the @cryptocom app.",
    "No matter how good the crypto chart look everytime I buy it reverses.",
    "I'll take #CRO and #MCO instead of love and happiness",
    "What is the biggest thing you bought with the @cryptocom card?",
    "Tips to new investors. Don't listen to me.=",
    "@cryptocom is my king. Take me with you to the moon oppa~~~~ #CRO",
    "I'm a crypto-sexual",
    "TSM > C9",
    "Who need to diversify in crypto when you have #CRO and #MCO",
    "I know exactly where my soul mate is. @cryptocom where are you keeping my icy white visa card",
    "#MCO and #CRO will be with me 10+ years from now. Hopefully with more baby #CRO and baby #MCO",
    "Crypto crash will destroy my profolio because I just invested, but I don't mind more opportunity to buy. I'm in for the long run",
    "Food or $15 in #CRO?",
    "Should I stop bathing to save money on hydro to buy more #CRO and #MCO? #Canada ",
    "@cryptocom could choke me and I would say thank you",
    "@cryptocom when will you come out with body pillow merch? #CRO #MCO",
    "I really need to plan for my future. Otherwise what would my future icy white @cryptocom card think of me.",
    "I want my future jobs to pay in #CRO",
    "Is it possible to be married to a metal visa card? #MCO #CRO",
    "How is kpop popular when @cryptocom exist? So many beautiful metal beings waiting to be snatch up",
    "I go to sleep happy knowing my baby @cryptocom icy white card is waiting for me",
    "I don't get how anyone could sell #CRO or #MCO",
    "I love the @cryptocom syndicate but sometime I feel bad for trading my baby #CRO to some other tokens",
    "I bought $1000 Amazon gift card for my family to use and got $50 back immediately @cryptocom #CRO",
    "When I buy a car the cashback will be beautiful #MCO #CRO",
    "I am so jealous of EU for having crypto.com cards before me. Please come to Canada faster",
    "I don't mind talking to a wall if it's about @cryptocom cards and #CRO",
    "Listening to vpop ballads!",
    "No amount of #CRO is ever enough. 5000 #MCO is enough because then I get my life time partner.",
    "How is everyone doing in the crypto-verse?",
    "Thanks god for blessing me with #CRO & mco visa",
    "I think @cryptocom mco visa need more colours",
    "can #CRO & #MCO moon already?",
    "Even in the top 10 cryptocurrencies #CRO is still being slept on",
    "#CRO to $1",
    "I want to be like that one guy that buy a house with mco visa",
    "Crypto.com is the king of crypto credit card. period. #CRO",
    "Where is the #MCO emoji?",
    "GIVEAWAY~~ If #CRO goes to $1 this year, i will pay everyone liking this 0 CRO each ($0)!",
    "Can scammer please just stop DMing me on @cryptocom telegram? Thanks. #CRO",
    "#crypto is the future",
    "Not sorry about being annoying with the referral because free #MCO",
    "At what level of syndicate oversubscription would it be better just put #CRO in the 20% interest stake?",
    "Should I take the bus or walk for free? $2 = ~14 #CRO",
    "Every time I buy something I think about how much #CRO & #MCO I could've bought with that money.",
    "can the bears just leave #CRO & #MCO alone? Better yet leave #crypto alone.",
    "@cryptocom 20% APR for staking #CRO would decrease at some point. Take advantage of this time.",
    "I will never use another card when I get my hands on @cryptocom mco visa card. Please ship to Canada faster.",
    "Is there anyone else in the @cryptocom fandom? #CRO #MCO",
    "@cryptocom is providing good rates to increase utilization. Think of it as a limited time promotion. #CRO #MCO",
    "@cryptocom please add more gift cards variety to canadians",
    "Being on twitter is depressing. Especially after seeing everyone with their mco cards.",
    "I hate how TD keep denying my crypto purchases #cryptocurrency #CRO #MCO #BTC",
    "Apologized to people irl who have to deal with my love for #cryptocurrency  #CRO & #MCO ",
    "altcoins giveth and alcoins taketh",
    "@cryptocom exchange need more volume #CRO #MCO #BTC",
    "Patience pays. Hopefully. #CRO #MCO #BTC",
    "Tweet about how I am bullish on #CRO #MCO #BTC",
    "FOMO is bad but missing out is also bad #CRO #MCO #BTC",
    "I will go on a shopping spree when I get the @cryptocom visa card. #CRO #MCO",
    "Can @TSM please win?",
    "@UofT is killing me. My love for #CRO & #MCO carry me through everyday",
    "Inspirational quote. #cryptocurrency #BTC #CRO #MCO",
    "Is there a cryptocon? #BTC #cryptocurrency",
    "@cryptocom is it possible to add compound interest option? I can't even manually add it into my earn because of the minimum amount required #MCO #CRO",
    "Can time travellers tell me when $BTC #CRO moon?",
    "I don't mind another stock market crash because then I get to buy cheap #BTC #CRO #MCO",
    "Can the stock market crash already? Thanks"
  ]

  while (True):
    # get the previous 75 tweets
    previous_tweets_objects = api.user_timeline(screen_name='@SEAN_CRO_FANBOY', count = 50, include_rts = True, tweet_mode="extended")
    previous_tweets = [[tweet.full_text.replace('\n','').replace('\n\n https://platinum.crypto.com/r/t8rqb2fyu2','')] for tweet in previous_tweets_objects]
    # choose a tweet that is not duplicate of previous 75 tweets
    tweet = ""
    tweet_chosen = False

    while(not tweet_chosen):
      tweet = random.choice(saved_tweets)
      if (tweet not in previous_tweets):
        tweet_chosen = True
        # a 20% to chance to add referral. Do not want to spam too much
        if (random.choice([0, 4]) == 0):
          tweet += "\n\n https://platinum.crypto.com/r/t8rqb2fyu2"
      else:
        return
    try:
      api.update_status(tweet)
    except tweepy.TweepError as error:
    #make exception for duplicate tweets
      if (error.api_code != 187):
        raise error
    # only post once every 2h-4h (7200 s to 14800)
    # to make the posting time seem more random
    time.sleep(random.choice([7200, 14800]))

if  __name__ =='__main__':main()