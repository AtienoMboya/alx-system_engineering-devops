#!/usr/bin/python3
"""Function to queries the first 10 hot posts for a given subreddit"""
import requests


def top_ten(subreddit):
    """
    queries the reddit api and prints the first 10 hot posts listed for a given
    subreddit
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
            "User-Agent": "linux: 0x16.api.advanced: v1.0.0\
            (by u/Charming-Zebra4864)"
            }
    params = {
            "limit": 10
            }
    response = requests.get(
            url, headers=headers, params=params,
            allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
