#!/usr/bin/python3
"""
    Write a function that queries the Reddit API and returns the number
     of subscribers (not active users, total subscribers) for a given
     subreddit. If an invalid subreddit is given, the function should return 0.
    import the requests library, which allows us to make HTTP requests to the
     Reddit API.
"""


def number_of_subscribers(subreddit):
    """
        A function that queries the Reddit API and returns the number of
        subscribers
    """

    import requests as req


    URL = f'https://www.reddit.com/r/{subreddit}/about.json'

    headers = {
        'User-Agent': 'Reddit-Agent'
    }

    response = req.get(URL, headers=headers)

    if (response.status_code == 200):
        Jstring = response.json()

        subs_count = Jstring['data']['subscribers']

        return subs_count
    else:
        return 0
