#!/usr/bin/python3
""" Exprting csv files"""
clientID = 'IUhfbGnPbZNfg1L0wQiFCg'
secretKey = 'HCVOhZOlLVuwJ2BmxFA6adstN9oT6g'
import json
import requests
import sys


def number_of_subscribers(subreddit):
	"""Read reddit API and return number subscribers """
	client_auth = requests.auth.HTTPBasicAuth(clientID, secretKey)
	username = 'sheraz-m-e'
	password = 'Reddit2024'
	data = {"grant_type": "password", "username": username, "password": password}
	user_pass_dict = {'user': username, 'passwd': password, 'api_type': 'json'}
	headers = {'user-agent': '/u/sheraz-m-e API Python for alx'}
	res = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=data, headers=headers)
	TOKEN = res.json()['access_token']
	print(TOKEN)
	headers = {**headers, **{'authorization': 'bearer {TOKEN}'}}
	url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
	client = requests.session()
	client.headers = headers
	print(client)
	r = client.get(url, allow_redirects=False)
	print(r)
	if r.status_code == 200:
		return (r.json()["data"]["subscribers"])
	else:
		return(0)
