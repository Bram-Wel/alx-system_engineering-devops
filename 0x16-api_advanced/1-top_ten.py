#!/usr/bin/python3
"""script for parsing web data from an api
"""
import requests


def top_ten(subreddit):
    """api call to reddit to get the number of subscribers
    """
    base_url = 'https://www.reddit.com/r/'
    headers = {
        'User-Agent':
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
         (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }
    url = base_url + '{}/top/.json?count=10'.format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    resp = json.loads(response.text)

    try:
        data = resp.get('data')
        children = data.get('children')
    except Exception as e:
        print('None')
    if children is None or data is None or len(children) < 1:
        print('None')

    for i, post_dict in enumerate(children):
        if i == 10:
            break
        print(post_dict.get('data').get('title'))
