#!/usr/bin/python3
"""
    Write a function that queries the Reddit API and returns the number
    of subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
        A function that queries the Reddit API and returns the number of
        subscribers
    """

    URL = f'https://www.reddit.com/r/{subreddit}/about.json'

    headers = {
        'User-Agent': 'Reddit-Agent'
    }

    response = requests.get(URL, headers=headers, allow_redirects=False)

    if (response.status_code == 200):
        Jstring = response.json()

        subs_count = Jstring['data']['subscribers']

        return subs_count
    else:
        return 0
