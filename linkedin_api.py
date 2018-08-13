import requests
import json
from urllib.parse import urlparse
import re

creds = json.loads(open('linkedin_secret.json').read())
auth_data={"response_type": "code",
           "client_id": creds['client_id'],
           "redirect_uri": creds['redirect_uri'],
           "state": "QF3hHuDaaG4jx4Ba",
           "scope": "r_basicprofile"
          } 
def getauth(auth_data=auth_data):
    auth_code = requests.get('https://www.linkedin.com/oauth/v2/authorization', params=auth_data)
    print("Go to linkedin url : " + auth_code.url)
    redirect_uri = input("Input the url of the redirected uri")
    o = urlparse(redirect_uri).query.split('&')
    auth_code = re.compile("^(?:code=)(.*)").search(o[0]).group(1)
    
    access_token_data={"grant_type": "authorization_code",
                       "code": auth_code,
                       "redirect_uri": creds['redirect_uri'],
                       "client_id": creds['client_id'],
                       "client_secret": creds['client_secret']}
    access_token = requests.post('https://www.linkedin.com/oauth/v2/accessToken', data=access_token_data )
    writetokenfile(access_token.json())
    return access_token

def refreshauth(auth_data=auth_data):
    auth_code = requests.get('https://www.linkedin.com/oauth/v2/authorization', params=auth_data)
    access_token_data={"grant_type": "authorization_code",
                       "code": auth_code,
                       "redirect_uri": creds['redirect_uri'],
                       "client_id": creds['client_id'],
                       "client_secret": creds['client_secret']}
    access_token = requests.post('https://www.linkedin.com/oauth/v2/accessToken', data=access_token_data )
    if access_token.status_code == 200:
        return access_token
    else:
        return False


def readtokefile(tokenfile='linkedin_token.json'):
    try:
        with open('linkedin_token.json') as f:
            return f.read()
    except:
        print('Unable to read file ' + tokenfile)

def writetokenfile(access_token, tokenfile='linkedin_token.json'):
    with open('linkedin_token.json', 'w+') as f:
        f.write(access_token.json())

file_token = readtokefile()
if not refreshauth():
    access_token = getauth()

