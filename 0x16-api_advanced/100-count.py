#!/usr/bin/python3
"""
    Write a recursive function that queries the Reddit API, parses the title
    of all hot articles, and prints a sorted count of given keywords
    (case-insensitive, delimited by spaces. Javascript should count
    as javascript, but java should not)
"""

import requests as req


def count_words(subreddit, word_list, after=None, results=None):
    """
        A recursive function that queries the Reddit API, parses the title of
        all hot articles, and prints a sorted count of given keywords
    """

    """ create dict to save results """
    if results is None:
        results = {}

    URL = f'https://www.reddit.com/r/{subreddit}/hot.json'

    headers = {
        'User-Agent': 'Something'
    }
    params = {
        'after': after
    }

    """ Send GET request to URL and save the response """
    response = req.get(URL, headers=headers, params=params,
                       allow_redirects=False)

    if (response.status_code != 200):
        return

    """ after parsing the response, save all hot titles is a list """
    data = response.json()['data']
    titles = [post['data']['title'] for post in data['children']]

    """ lowercase and split title words to a list """
    for title in titles:
        Twords = title.lower().split()
        """ compare each user word with the title list and count """
        for word in word_list:
            word_count = Twords.count(word)
            if (word_count > 0):
                results[word] = results.get(word, 0) + word_count

    """ If there is no after page, return values """
    if not data['after']:
        """ Sort the results """
        sorted_lst = sorted(results.items(), key=lambda kv:
                            (-kv[1], kv[0].lower()))
        """ print out resultes """
        for word, count in sorted_lst:
            if (count > 0):
                print(f'{word.lower()}: {count}')
    else:
        return count_words(subreddit, word_list, after=data['after'],
                           results=results)
