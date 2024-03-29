#!/usr/bin/python3
"""
    Write a function that queries the Reddit API and returns the number
    of subscribers for a given subreddit. If an invalid subreddit is given,
    the function should return 0
"""

import requests as req


def number_of_subscribers(subreddit):
    """
        A function that queries the Reddit API and returns the number of
        subscribers
    """

    URL = f'https://www.reddit.com/r/{subreddit}/about.json'

    headers = {
        'User-Agent': 'Reddit-Agent'
    }

    response = req.get(URL, headers=headers, allow_redirects=False)

    if (response.status_code == 200):
        Jstring = response.json()

        return Jstring['data']['subscribers']
    else:
        return 0
