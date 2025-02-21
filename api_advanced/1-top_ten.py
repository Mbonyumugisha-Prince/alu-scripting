#!/usr/bin/python3
"""Module to query Reddit API and get top 10 hot posts of a subreddit"""
import requests


def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.

    Args:
        subreddit (str): The subreddit to search.

    Returns:
        None. Prints either the titles or None if subreddit is invalid.
    """
    # Reddit API endpoint for hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    
    # Custom User-Agent to avoid Too Many Requests error
    headers = {
        'User-Agent': 'linux:reddit_top_ten:v1.0.0 (by /u/your_username)'
    }
    
    # Parameters to limit number of posts and prevent redirect
    params = {
        'limit': 10,
        'allow_redirects': False
    }
    
    try:
        # Make GET request to Reddit API
        response = requests.get(url, headers=headers, params=params)
        
        # Check if subreddit exists
        if response.status_code == 404:
            print(None)
            return
        # Check if we got a successful response
        if response.status_code != 200:
            print(None)
            return
            
        # Parse response JSON
        data = response.json()
        
        # Extract and print post titles
        posts = data['data']['children']
        for post in posts:
            print(post['data']['title'])
            
    except Exception:
        print(None)
