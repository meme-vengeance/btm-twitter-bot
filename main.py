import time
import tweepy
from TextSpamBot import TextSpamBot


def read_credentials(fname='credentials.txt'):
    """Reads a file for a list of credentials. Each set of four lines in the
    file must contain the items:
        CONSUMER_KEY
        CONSUMER_SECRET
        ACCESS_KEY
        ACCESS_SECRET
    :param fname: credentials filename
    :return: a list of lists of string, where each list contains one new
    credential
    """
    with open(fname, 'r') as f:
        lines = f.readlines()
    content_lines = list(filter(lambda l: l.strip() != '', lines))
    all_creds = []
    while len(content_lines) >= 4:
        all_creds.append(content_lines[:4])
        content_lines = content_lines[4:]
    return all_creds


def new_api(credentials):
    """Given a list of length 4 containing
            [CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET],
    returns a new twitter api object
    """
    consumer_key, consumer_secret, access_key, access_secret = credentials
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    return tweepy.API(auth)


if __name__ == '__main__':
    # Read list of credentials from text file
    all_creds = read_credentials('credentials.txt')
    # Get first credentials
    current_cred = all_creds[0]
    # Initiate twitter api for this account
    api = new_api(current_cred)
    # Start a text spam bot
    spam_bot = TextSpamBot(twitter_api=api, text_file='lines.txt')
    spam_bot.start()
    # Spam text every 60 seconds
    while True:
        spam_bot.loop()
        time.sleep(60)

