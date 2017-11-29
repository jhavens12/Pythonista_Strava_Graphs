#v1.0
import requests
import json
import credentials

def my_activities():
    url = 'https://www.strava.com/api/v3/athlete/activities'
    header = {'Authorization': 'Bearer '+credentials.api_key}
    param = {'per_page':200, 'page':1}
    my_dataset = requests.get(url, headers=header, params=param).json()
    return my_dataset

def activities():
    url = 'https://www.strava.com/api/v3/activities/following'
    header = {'Authorization': 'Bearer '+credentials.api_key}
    param = {'per_page':200, 'page':1}
    dataset = requests.get(url, headers=header, params=param).json()
    return dataset
