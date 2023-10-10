#!/usr/bin/python3
"""
    Write a function that queries the Reddit API and returns the number
    of subscribers for a given subreddit.
"""


def number_of_subscribers(subreddit):
    """
        A function that queries the Reddit API and returns the number of
        subscribers
    """

    import requests

    
    URL = f'https://www.reddit.com/r/{subreddit}/about.json'

    headers = {
        'User-Agent': 'Reddit-Agent'
    }

    response = requests.get(URL, headers=headers)

    if (response.status_code == 200):
        Jstring = response.json()

        subs_count = Jstring['data']['subscribers']

        return subs_count
    else:
        return 0
