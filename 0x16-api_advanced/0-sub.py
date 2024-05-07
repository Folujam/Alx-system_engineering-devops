#!/usr/bin/python3
"""queries the Reddit API"""

import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers={'User-Agent': 'my-app'})
    try:
        return response.json()['data']['subscribers']
    except Exception:
        return 0
