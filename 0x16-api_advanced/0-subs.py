#!/usr/bin/python3
""" 0. How many subs? """

from requests import get


def number_of_subscribers(subreddit):
    """Number of subs function"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    r = get(url).json()
    if r.get('kind') != 't5':
        return 0
    data = r.get('data')
    return data['subscribers']
