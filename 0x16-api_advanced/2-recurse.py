#!/usr/bin/python3
""" 0. How many subs? """

from requests import get

headers = {'User-Agent': 'My User Agent'}


def recurse(subreddit, hot_list=[], after=""):
    """Number of subs function"""

    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
        subreddit, after)
    response = get(url, headers=headers, allow_redirects=False)
    if response.status_code is not 200:
        return hot_list
    r = response.json()
    data = r.get('data')
    children = data['children']
    for i in range(len(children)):
        hot_list.append(children[i].get('data')['title'])
    after = data['after']
    if after is not None:
        recurse(subreddit, hot_list, after)
    return hot_list
