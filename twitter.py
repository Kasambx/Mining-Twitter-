pip install twitter 

# XXX: Go to http://dev.twitter.com/apps/new to create an app and get values
# for these credentials, which you'll need to provide in place of these
# empty string values that are defined as placeholders.
# See https://dev.twitter.com/docs/auth/oauth for more information
# on Twitter's OAuth implementation.
import twitter 

CONSUMER_KEY ='kzRk04Y50hL5kT7nmoMsXt8yT'
CONSUMER_SECRET= '5KIMSPt94ZZYvbClH7TDlZWQqEAG36edllNLy9OUgi1EV7ktql'
OAUTH_TOKEN= ''
OAUTH_TOKEN_SECRET = ''

auth = twitter .oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET )

twitter_api = twitter.Twitter(auth=auth)

# Nothing to see by displaying twitter_api except that it's now a
# defined variable
print twitter_api



