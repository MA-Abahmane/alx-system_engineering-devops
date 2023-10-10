#!/usr/bin/python3
"""
    Write a recursive function that queries the Reddit API and returns a
    list containing the titles of all hot articles for a given subreddit.
    If no results are found, the function should return None.
"""

import requests as req


def recurse(subreddit, hot_list=[], after=None, count=0):
    """
        A recursive function that queries the Reddit API and returns a
        list containing the titles of all hot articles for a given subreddit
    """

    URL = f'https://www.reddit.com/r/{subreddit}/hot/.json'

    headers = {
        'User-Agent': 'Reddit'
    }
    params = {
        'limit': 100,
        'count': count,
        'after': after
    }

    response = req.get(URL, headers=headers, params=params,
                       allow_redirects=False)

    if (response.status_code == 200):
        Jstring = response.json()

        data = Jstring['data']
        after = data['after']
        count += data['dist']

        hot_list.extend([post['data']['title'] for post in data['children']])

    else:
        return None

    if (after):
        return recurse(subreddit, hot_list, after, count)
    else:
        return hot_list
