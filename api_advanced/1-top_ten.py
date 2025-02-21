#!/usr/bin/python3
"""Module for querying Reddit API"""
import requests


def top_ten(subreddit):
    """Queries the Reddit API and prints titles of first 10 hot posts
    for a given subreddit.

    Args:
        subreddit: name of the subreddit to query
    """
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    headers = {'User-Agent': 'Custom/0.0.1'}
    params = {'limit': 10}

    response = requests.get(url, headers=headers, params=params,
                          allow_redirects=False)

    if response.status_code >= 300:
        print('None')
        return

    results = response.json().get('data', {}).get('children', [])

    if not results:
        print('None')
        return

    for post in results:
        print(post.get('data', {}).get('title'))
