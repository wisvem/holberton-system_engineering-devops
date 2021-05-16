#!/usr/bin/python3
""" 0. How many subs? """

from requests import get

headers = {'User-Agent': 'My User Agent'}


def recurse(subreddit, hot_list=[]):
    """Number of subs function"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    response = get(url, headers=headers, allow_redirects=False)
    if response.status_code is not 200:
        return print('None')

    r = response.json()
    data = r.get('data')
    children = data['children']
    for i in range(10):
        print(children[i].get('data')['title'])
