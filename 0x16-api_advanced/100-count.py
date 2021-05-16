#!/usr/bin/python3
""" 0. How many subs? """

from requests import get

headers = {'User-Agent': 'My User Agent'}


def validate_word_dict(word_dict, word_list):
    """Validate word dict"""
    for word in word_list:
        if word.lower() not in word_dict:
            word_dict[word.lower()] = 0
    return word_dict


def count_words(subreddit, word_list):
    """Count words main function"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(
        subreddit)
    response = get(url, headers=headers, allow_redirects=False)
    if response.status_code is not 200:
        return None
    result = recursive_count(subreddit, word_list, '', {})
    for k, v in sorted(result.items(), key=lambda x: (-x[1], x[0])):
        if v is not 0:
            print("{}: {}".format(k, v))
    return None


def recursive_count(subreddit, word_list, after='', word_dict={}):
    """Number of subs function"""
    word_dict = validate_word_dict(word_dict, word_list)
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
        subreddit, after)
    response = get(url, headers=headers, allow_redirects=False)
    if response.status_code is not 200:
        return None
    r = response.json()
    data = r.get('data')
    children = data['children']
    title_list = []
    # get every title
    for i in range(len(children)):
        title_list.append(children[i].get('data')['title'].lower())

    for title in title_list:
        for key in word_list:
            for x in title.split(' '):
                if key.lower() == x.lower():
                    word_dict[key.lower()] += 1

    after = data['after']
    if after is not None:
        recursive_count(subreddit, word_list, after, word_dict)
    return word_dict
