
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
    headers = {'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
    url = f"https://api.reddit.com/r/{subreddit}/about"
    resp = requests.get(url, headers, allow_redirects=False)

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
