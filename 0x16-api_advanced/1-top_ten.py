#!/usr/bin/python3
"""queries the Reddit API"""

import requests


def top_ten(subreddit):
    """
    prints top ten post titles listed
    """
    if subreddit is None or type(subreddit) is not str:
        print(None)

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    head = {'User-Agent': 'my-app'}
    parameter = {'limit': 10}
    response = requests.get(url, headers=head, params=parameter)
    posts = response.json().get('data').get('children')
    if posts is None or (len(posts) > 0 and posts[0].get('kind') != 't3'):
        print(None)
    else:
        for post in posts:
            print(post.get('data').get('title'))
