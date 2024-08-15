#!/usr/bin/python3
"""querie the Reddit API and returns the number of subscribers"""

import json
import requests
import sys

def number_of_subscribers(subreddit):
	url = 'https://reddit.com/r/{}/about.json'.format(subreddit)
	headers = {"User-Agent": "Mozilla/5.0"}

	response = requests.get(url, headers=headers, allow_redirects=False)
	if response.status_code == 404:
		return 0
	results = response.json().get("data")
	return results.get("subscribers")
