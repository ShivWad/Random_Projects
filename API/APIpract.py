import requests
import json
from requests.auth import HTTPBasicAuth
##GET request
def getRequest (client_id , state , redirect_uri , scope):
    info_get = {'client_id': client_id, 'response_type': 'code',
                'state': state, 'redirect_uri': redirect_uri,
                'scope': scope}
    Get_req = requests.get('https://www.reddit.com/api/v1/authorize.compact?' ,params = info_get )
    print(Get_req.url)

##Post request
def postRequest (auth_code, redirect_uri , secret , client_id , UserAgent):
    info_post = {'grant_type': 'authorization_code', 'code': auth_code,
                 'redirect_uri': redirect_uri}
    Post_req = requests.post('https://www.reddit.com/api/v1/access_token' , data = info_post ,
                         auth = (client_id , secret),
                         headers = {'User-Agent' : UserAgent})
    print(Post_req.text)
#API_REQ
def BestofReddit (userAgent, accessToken):
    header_API = {'User-Agent' : userAgent , 'Authorization': 'bearer ' + accessToken}
    Api_req = requests.get('https://oauth.reddit.com/best' , headers = header_API )
    data = Api_req.json()
    return data

def HotofReddit (UserAgent, accessToken):
    header_API = {'User-Agent': UserAgent, 'Authorization': 'bearer ' + accessToken}
    Api_req = requests.get('https://oauth.reddit.com/hot', headers=header_API)
    data = Api_req.json()
    return data

def NewofReddit (userAgent, accessToken):
    header_API = {'User-Agent': userAgent, 'Authorization': 'bearer ' + accessToken}
    Api_req = requests.get('https://oauth.reddit.com/new', headers=header_API)
    data = Api_req.json()
    return data

def Get_Subreddit_Info (subreddit ,accessToken):
    header_API = {'User-Agent': userAgent, 'Authorization': 'bearer ' + accessToken}
    Api_req = requests.get('https://oauth.reddit.com/r/'+subreddit+'/about', headers = header_API)
    data = Api_req.json()
    return data

def Subscribe (subreddit, useragent, accessToken):
    header_API = {'User-Agent': useragent, 'Authorization': 'bearer ' + accessToken}
    Api_req = requests.post('https://oauth.reddit.com/subscribe', headers=header_API , params={'action' :'sub', 'sr' : subreddit})
    data = Api_req.json()
    print(Api_req.url)
    return data
#Sample Data
def GeTInfo (data):
    children = data['data']['children']
    print( "Authors : Titles : No of Comments")
    for d in children:
        print(d['data']['author'], " : ", d['data']['title'] , " : ", d['data']['num_comments'] )
        print('---------------------------------------------')



info = Subscribe('Music','UserAgent','')
print(info)