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
    writetokenfile(access_token)
    return access_token.json()

def readtokefile(tokenfile='linkedin_token.json'):
    try:
        with open('linkedin_token.json') as f:
            return f.read()
    except:
        print('Unable to read file ' + tokenfile)

def writetokenfile(access_token, tokenfile='linkedin_token.json'):
    with open('linkedin_token.json', 'w+') as f:
        # writes access token in json format
        f.write(str(json.dumps(access_token.json())))

def testtoken(token):
    access_token = json.loads(token)['access_token'] 
    headers= { 'Authorization': 'Bearer ' + access_token }
    client = requests.get('https://api.linkedin.com/v1/people/~', headers=headers)
    return client.ok

def getcurrentprofile(token):
    headers= { 'Authorization': 'Bearer ' + access_token['access_token'], 
               'x-li-format': 'json'
             }
    client = requests.get('https://api.linkedin.com/v1/people/~', headers=headers )
    if client.ok:
        return client.json()

file_token = readtokefile()
if file_token is None:
    access_token = getauth()
else:
    if not testtoken(file_token):
        access_token = getauth()
    else:
        access_token = json.loads(file_token)

getcurrentprofile(access_token)

