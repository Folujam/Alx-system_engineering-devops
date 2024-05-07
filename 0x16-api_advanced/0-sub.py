#!/usr/bin/python3
"""queries the Reddit API"""

import requests


def number_of_subscribers(subreddit):
    """
    returns the number of subscribers
    """
    if subreddit is None or type(subreddit) is not str:
        return 0

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    head = {'User-Agent': 'my-app'}
    response = requests.get(url, headers=head, allow_redirects=False)

    if response.status_code == 200:
        return (response.json().get("data").get("subscribers"))
