#!/usr/bin/python3
"""
Using Reddit's API to retrieve top post titles from a subreddit.
"""
import requests

after = None


def recurse(subreddit, hot_list=[]):
    """
    Recursively retrieve top post titles from a subreddit.

    Args:
        subreddit (str): The subreddit name.
        hot_list (list): List to store post titles.

    Returns:
        list: List containing top post titles.
    """
    global after
    user_agent = {'User-Agent': 'api_advanced-project'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    parameters = {'after': after}

    results = requests.get(url, params=parameters,
                           headers=user_agent, allow_redirects=False)

    if results.status_code == 200:
        after_data = results.json().get("data").get("after")

        if after_data is not None:
            after = after_data
            recurse(subreddit, hot_list)

        all_titles = results.json().get("data").get("children")
        for title_ in all_titles:
            hot_list.append(title_.get("data").get("title"))

        return hot_list
    else:
        return None
