#!/usr/bin/python3
"""
    Write a function that queries the Reddit API and prints the titles of the
    first 10 hot posts listed for a given subreddit
"""

import requests as req


def top_ten(subreddit):
    """
    A function that queries the Reddit API and prints the titles of the
    first 10 hot posts
    """

    URL = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'

    headers = {
        'User-Agent': 'Reddit-Agent'
    }

    response = req.get(URL, headers=headers, allow_redirects=False)

    if (response.status_code >= 300):
        print(None)
    else:
        Js = response.json()
        [print(child.get("data").get("title")) for child in Js.get("data").get("children")]
