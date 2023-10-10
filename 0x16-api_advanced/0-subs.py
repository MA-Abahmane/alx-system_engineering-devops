#!/usr/bin/python3
"""
    Write a function that queries the Reddit API and returns the number
     of subscribers (not active users, total subscribers) for a given
     subreddit. If an invalid subreddit is given, the function should return 0.
    import the requests library, which allows us to make HTTP requests to the
     Reddit API.
"""

import requests


def number_of_subscribers(subreddit):
    """
        A function that queries the Reddit API and returns the number of
        subscribers
    """

    if subreddit is None or type(subreddit) is not str:
        return 0

    URL = f'https://www.reddit.com/r/{subreddit}/about.json'


    headers = {
        'User-Agent': 'Reddit-Agent'
    }

    response = requests.get(URL, headers=headers, allow_redirects=False)


    if (response.status_code >= 300):
        return 0

    subs_count = response.json().get("data").get("subscribers")

    return subs_count