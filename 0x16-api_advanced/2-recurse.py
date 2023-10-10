#!/usr/bin/python3
"""
    Write a recursive function that queries the Reddit API and returns a
     list containing the titles of all hot articles for a given subreddit.
     If no results are found for the given subreddit, the function should
     return None.
    import the requests library, which allows us to make HTTP requests to
     the Reddit API.
"""

import requests as req


def recurse(subreddit, hot_list=[], after=None, count=0):
    """
        A recursive function that queries the Reddit API and returns a
        list containing the titles of all hot articles for a given subreddit
    """

    # By appending "/about.json" to the subreddit's URL, we can access various
    #  details about the subreddit, including its number of subscribers,
    #  description and more, in a structured JSON format.
    URL = f'https://www.reddit.com/r/{subreddit}/hot/.json'

    # Define a custom user agent to avoid too many requests error
    headers = {
        'User-Agent': 'Reddit'
    }
    # saved parameters
    params = {
        'limit': 100,
        'count': count,
        'after': after
    }

    # sending a GET request to reddits API
    response = req.get(URL, headers=headers, params=params,
                       allow_redirects=False)

    # successful request
    if (response.status_code == 200):
        # parse the response to a json string
        Jstring = response.json()

        data = Jstring['data']
        # next page to search
        after = data['after']
        # number of elements in children (Titles)
        count += data['dist']

        # get titles from current page:
        hot_list.extend([post['data']['title'] for post in data['children']])

    else:
        return None

    # if a next pae exists, recurse
    if (after):
        return recurse(subreddit, hot_list, after, count)
    else:
        return hot_list
