import requests
import os


def make_github_call(query):
    url = 'https://api.github.com/graphql'
    json = {"query": query}
    api_token = os.getenv("GITHUB_ACCESS_TOKEN")
    headers = {'Authorization': 'token %s' % api_token}
    res = requests.post(url=url, json=json, headers=headers)
    return res.json()
