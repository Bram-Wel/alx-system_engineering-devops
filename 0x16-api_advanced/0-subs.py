#!/usr/bin/python3
"""
Contains function number_of_subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """Query the Reddit API"""
    user_agent = "android:com.example.myredditapp:v1.2.3 (by /u/kemitche)"
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
        # except requests.exceptions.JSONDecodeError as e:
        except Exception:
            # print(e)
            return 0
        return number
