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

    # By appending "/about.json" to the subreddit's URL, we can access various
    #  details about the subreddit, including its number of subscribers,
    #  description and more, in a structured JSON format.
    URL = f'https://www.reddit.com/r/{subreddit}/about.json'

    # Define a custom user agent to avoid too many requests error
    headers = {
        'User-Agent': 'Reddit-Agent'
    }

    # sending a GET request to reddits API
    response = requests.get(URL, headers=headers, allow_redirects=False)

    # error handling
    if (response.status_code >= 300):
        return 0

    # parse the response to a json string
    subs_count = response.json().get("data").get("subscribers")

    return subs_count
