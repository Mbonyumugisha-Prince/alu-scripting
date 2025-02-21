#!/usr/bin/python3
"""
Script to print hot posts on a given Reddit subreddit.
"""

import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/your_username)"
    }

    params = {"limit": 10}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)

        # Handle HTTP errors
        if response.status_code != 200:
            print("None")
            return

        # Ensure response contains valid JSON
        try:
            data = response.json()
        except ValueError:
            print("None")
            return

        # Extract posts and print their titles
        results = data.get("data", {})
        for post in results.get("children", []):
            print(post["data"]["title"])

    except requests.RequestException:
        print("None")

