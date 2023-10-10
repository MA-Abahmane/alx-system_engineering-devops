#!/usr/bin/python3
"""
    Write a recursive function that queries the Reddit API, parses the title of
    all hot articles, and prints a sorted count of given keywords (case-insensitive,
    delimited by spaces. Javascript should count as javascript, but java should not)
"""

import requests


def count_words(subreddit, word_list, after=None, results=None):
    """
        A recursive function that queries the Reddit API, parses the title of
        all hot articles, and prints a sorted count of given keywords
    """

    if results is None:
        results = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    headers = {
        "User-Agent": "My-User-Agent"
    }
    params = {
        "after": after
    }

    response = requests.get(url, params=params, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json().get("data")
    hot_titles = [post["data"]["title"] for post in data.get("children")]

    for title in hot_titles:
        words = title.lower().split()
        for word in word_list:
            word_count = words.count(word.lower())
            if word_count > 0:
                results[word] = results.get(word, 0) + word_count

    if not data.get("after"):
        # Sort the results as specified
        sorted_results = sorted(results.items(), key=lambda kv: (-kv[1], kv[0].lower()))
        for word, count in sorted_results:
            if count > 0:
                print(f"{word.lower()}: {count}")
    else:
        return count_words(subreddit, word_list, after=data.get("after"), results=results)
