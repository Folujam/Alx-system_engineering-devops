#!/usr/bin/python3
"""queries the Reddit API"""

import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers={'User-Agent': 'my-app'})
    if response.status_code == 200:
        return (response.json().get('data').get('subscribers'))
    return (0)
