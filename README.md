# TwitterCryptoPromotionBot
A python bot to promote my crypto.com referral code
https://twitter.com/SEAN_CRO_FANBOY

Bot is deployed on server using Docker and AWS
- [x] auto tweet
- [x] auto reweet and favourite

Steps to deploy:

1: Build and test image:
  - docker build . -t twitter_bot
  - docker run -it twitter_bot
  
2: Export image:
  - docker image save twitter_bot:latest -o twitter_bot.tar
  - gzip twitter_bot.tar
  
3: Create EC2 instance on AWS and connect to instance on local computer
  - create utuntu instance
  - connect to instance after it's running on AWS by right clicking in the instance and follow the steps in connect
  - download docker on instance by running
     -sudo apt-get update
     -sudo apt install docker.io
     -sudo adduser ubuntu docker
     -exit
  

4: Upload image
  - scp -i "pem file downloaded whencreating EC2 instanced" twitter_bot.tar.gz ubuntu@ec2-3-86-66-73.compute-1.amazonaws.com:/tmp
  (ubuntu@ec2-3-86-66-73.compute-1.amazonaws.com based on base image chosen when creating EC2 instance)
  - login to EC2 instance on local computer
  - gunzip /tmp/twitter_bot.tar.gz
  - docker image load -i /tmp/twitter_bot.tar
  
5: Run image
  - docker run -d --restart always twitter_bot
