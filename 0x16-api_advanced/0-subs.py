#!/usr/bin/python3
"""
Contains function number_of_subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers of a subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': "My user agent 1.0"}
    subreddit_data = requests.get(url, allow_redirects=False, headers=headers)
    if subreddit_data.status_code == 404:
        return 0
    number_of_subscribers = subreddit_data.json()['data']['subscribers']
    return number_of_subscribers
