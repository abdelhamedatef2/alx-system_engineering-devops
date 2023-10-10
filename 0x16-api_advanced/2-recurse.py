#!/usr/bin/python3
"""recurse module"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """Return: Li containing titles of all hot article for given subreddit,
    None if no result found
    """
    r = requests.get("https://reddit.com/r/{}/hot.json?after={}".
                     format(subreddit, after),
                     headers={"User-agent": "custom"})

    if r.status_code != 200:
        return None
    if after is None:
        return hot_list

    for i in r.json().get("data").get("children"):
        hot_list.append(i.get("data").get("title"))
    after = r.json().get("data").get("after")

    return recurse(subreddit, hot_list, after)
