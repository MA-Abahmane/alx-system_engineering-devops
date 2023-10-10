#!/usr/bin/python3
"""
    Write a function that queries the Reddit API and prints the titles of the
     first 10 hot posts listed for a given subreddit.
    import the requests library, which allows us to make HTTP requests to the
     Reddit API.
"""

import requests as req


def top_ten(subreddit):
    """
        a function that queries the Reddit API and prints the titles of the
         first 10 hot posts
    """

    # By appending "/about.json" to the subreddit's URL, we can access various
    #  details about the subreddit, including its number of subscribers,
    #  description and more, in a structured JSON format.
    URL = f'https://www.reddit.com/r/{subreddit}/hot.json'

    # Define a custom user agent to avoid too many requests error
    headers = {
        'User-Agent': 'Reddit'
    }

    # sending a GET request to reddits API
    response = req.get(URL, headers=headers, allow_redirects=False)

    # successful request
    if (response.status_code == 200):
        # parse the response to a json string
        Jstring = response.json()

        # extract  the chrldrent from data if exists
        # then extract the top 10 titles from children data
        if 'data' in Jstring and 'children' in Jstring['data']:
            posts = Jstring['data']['children']
            for i, post in enumerate(posts):
                if i <= 9:
                    title = post['data']['title']
                    print(title)
        else:
            print('None')
    # in case of error
    else:
        print('None')
