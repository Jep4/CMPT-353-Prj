
# main code start
import twitter, time

# twitter api connect
twitter_consumer_key = 'xE2KeJ6dd98hHSR5XOmPr615K'
twitter_consumer_secret = 'IDiGtGAgjUePiQcjZH2ODOfkYC2ytwkhbM0Pr5EBwv7qGeyxz9'
twitter_access_token = '1589819209575698432-T7I2dl9tmGrlWNQxyyhgzUWnbx5nGn'
twitter_access_secret = 'YcsAwIs6KUmMUlZXowgKruavACoRIh2mGgU4tT7xrOvQJ'

twitter_api = twitter.Api(consumer_key=twitter_consumer_key,
                          consumer_secret=twitter_consumer_secret, 
                          access_token_key=twitter_access_token, 
                          access_token_secret=twitter_access_secret)
query = "gun ownership"
search = twitter_api.GetSearch(term=query, count=100) 

for i in search:
    print(i.text) 