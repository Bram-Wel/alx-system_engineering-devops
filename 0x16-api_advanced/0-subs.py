#!/usr/bin/python3
"""
This module describes a query function
"""
import requests


def number_of_subscribers(subreddit):
    """Query the Reddit API.

    Args:
        @subredit: The type of resource/object requested
    Return:
        The number of subscribers for the subreddit, or 0 if
    """
    user_agent = "User-Agent: android:com.example.myredditapp:v1.2.3\
 (by /u/kemitche)"
    # print(user_agent)
    headers = {'user-agent': user_agent}
    url = f"https://api.reddit.com/r/{subreddit}/about"
    resp = requests.get(url, headers=headers, allow_redirects=False)

    try:
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        # print(e)
        return 0
    else:
        try:
            number = resp.json().get('data')['subscribers']
        except requests.exceptions.JSONDecodeError as e:
            # print(e)
            return 0
        return number
