#!/usr/bin/python3
"""queries Reddit API"""

import requests
after = None


def recurse(subreddit, hot_list=[]):
    """
    returns a list containing the titles of all hot articles for the subreddit
    or None if queried subreddit is invalid
    """
    global after
    if subreddit is None or type(subreddit) is not str:
        return None
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    head = {'User-Agent': 'my-app'}
    parameter = {'after': after}
    response = requests.get(url, headers=head, params=parameter)
    if response.status_code == 200:
        next_ = response.json().get('data').get('after')
        if next_ is not None:
            after = next_
            recurse(subreddit, hot_list)
        list_titles = response.json().get('data').get('children')
        for title_ in list_titles:
            hot_list.append(title_.get('data').get('title'))
        return hot_list
    else:
        return (None)
