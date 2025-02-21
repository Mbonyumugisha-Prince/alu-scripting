#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""
import json
import requests
import sys


def top_ten(subreddit):
    """Get the top ten hot posts of a subreddit
    Args:
        subreddit: the subreddit to search
    Returns:
        None if subreddit is invalid, otherwise prints the titles
    """
    # Set custom User-Agent to avoid rate limiting
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    
    # Reddit API URL
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    
    try:
        # Make request and set allow_redirects to False
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if response is successful and not a redirect
        if response.status_code != 200:
            print(None)
            return
            
        # Parse response and print titles
        data = response.json().get('data', {}).get('children', [])
        for post in data:
            print(post.get('data', {}).get('title'))
            
    except Exception:
        print(None)
