#!/usr/bin/python3
"""This module describes a query freturn."""

import requests


def number_of_subscribers(subreddit):
    """Query the Reddit API.

    Args:
        @subredit: The type of resource/object requested
    Return:
        The number of subscribers for the subreddit, or 0 if
    """
    resp = requests.get(f"https://api.reddit.com/r/{subreddit}/about", headers={'user-agent': 'Bram'}, allow_redirects=False)

    try:
        resp.raise_for_status()
    except requests.exceptions.HTTPError:
        return 0
    else:
        try:
            number = resp.json().get('data')['subscribers']
        except requests.exceptions.JSONDecodeError:
            return 0
        return resp.json().get('data')['subscribers']
