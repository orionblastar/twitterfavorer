# Original by James Morris JMOZ at: http://blog.jmoz.co.uk/increase-your-twitter-followers/
# Modified by Eris Blastar http://iwethey.neocities.org/ erisblastar@gmail.com to encode UTF-8 strings in case
# of foriegn language and odd characters. 
# Modified for Python 3 just do sudo pip3 install twitter
# Python 3 mods by Orion Blastar orionblastar@gmail.com http://blastar.in/
# You need your API key from https://dev.twitter.com/discussions/631 and make sure it isn't set to
# read-only when you make the access token.
# Good luck, Eris & Orion.

from twitter import Twitter, OAuth, TwitterHTTPError
# -*- coding: utf-8 -*-
import sys
 
 
OAUTH_TOKEN = 'foo'
OAUTH_SECRET = 'bar'
CONSUMER_KEY = 'bat'
CONSUMER_SECRET = 'buzz'
 
t = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET, CONSUMER_KEY, CONSUMER_SECRET))
 
 
def search_tweets(q, count=100, max_id=None):
    return (t.search.tweets(q=q, result_type='recent', count=count, lang="en", max_id=max_id))
 


def favorites_create(tweet):
    try:
        result = t.favorites.create(_id=tweet['id'])
        print ("Favorited: %s, %s" % (result['text'].encode(sys.stdout.encoding, errors='replace'), result['id']))
        return (result)
    except TwitterHTTPError as e:
        print ("Error: ", e)
        return None


 
def search_and_fav(q, count=100, max_id=None):
    result = search_tweets(q, count, max_id)
    first_id = result['statuses'][0]['id']
    last_id = result['statuses'][-1]['id']
    success = 0
    
    for t in result['statuses']:
        if favorites_create(t) is not None:
            success += 1
 
    print("Favorited total: %i of %i" % (success, len(result['statuses'])))
    print("First id %s last id %s" % (first_id, last_id))