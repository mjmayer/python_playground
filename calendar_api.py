import requests
import requests_oauthlib
import json
import pprint

#import client oauth
authfile = json.loads(open("client_id.json").read())

#setup auth variables
CLIENT_ID = ''
CLIENT_SECRET = ''
REDIRECT_URI = 'https://www.mayerinformatics.com/'
TOKEN_URL = "https://accounts.google.com/o/oauth2/token"
TOKENFILE = "token"
GC_BASEURL = 'https://www.googleapis.com/calendar/v3'

def gettoken (client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI):
    scope = ['https://www.googleapis.com/auth/calendar']
    oauth = requests_oauthlib.OAuth2Session(client_id, redirect_uri=redirect_uri,
                         scope=scope)
    
    authorization_url, state = oauth.authorization_url(
            'https://accounts.google.com/o/oauth2/auth',
            # access_type and prompt are Google specific extra
            # parameters.
            access_type="offline", prompt="select_account")
    print('Please go to %s and authorize access.' % authorization_url)
    
    # Get the authorization verifier code from the callback url
    authorization_response = raw_input('Enter the full callback URL')
    
    token = oauth.fetch_token(
            'https://accounts.google.com/o/oauth2/token',
            authorization_response=authorization_response,
            # Google specific extra parameter used for client
            # authentication
            client_secret=client_secret)
    #saves token to disk
    tokensaver(token)

# Write token to file
def tokensaver(token):
    with open(TOKENFILE, "w") as tokenfile:
        tokenfile.write(str(token))

def readtoken (tokenfile=TOKENFILE):
    try:
        with open(tokenfile) as t:
            token_dict = eval(t.read())
            token = token_dict
        return token
    except OSError:
        print('Unable to read %s', tokenfile)

tokenfromfile = readtoken(tokenfile=TOKENFILE)

if tokenfromfile is None:
    gettoken()
    tokenfromfile = readtoken(tokenfile=TOKENFILE)

#refresh token
extra = {
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET
    }
client = requests_oauthlib.OAuth2Session(CLIENT_ID, token=tokenfromfile, auto_refresh_url=TOKEN_URL,
                       auto_refresh_kwargs=extra, token_updater=tokensaver)

callist = client.get(GC_BASEURL + '/users/me/calendarList')
callist = json.loads(callist.content)
for c in callist['items']:
    if (c['summary']) == "Todoist":
       todoistcal = c


#c = client.get(GC_BASEURL + '/calendars/primary')
#print(c.content)
