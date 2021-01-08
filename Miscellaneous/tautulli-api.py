#!/usr/bin/env python3

import requests
import json

# API key on file on local machine for security
api_key = ""
api_prepath="/home/docker/code/" # Update this if run on different machine
with open(api_prepath + "PythonRepository/Miscellaneous/api.txt", "r") as f:
	api_key = str.strip(f.read())
	
def get_watched_time(days, userlist):
	"""
	Gets watch data based on user and days specified
	"""
	watch_list = []
	# API data at https://github.com/Tautulli/Tautulli-Wiki/wiki/Tautulli-API-Reference
	url = f"http://10.0.0.126:8181/api/v2?apikey={api_key}&cmd=get_user_watch_time_stats&query_days={days}&user_id="
	for i in userlist:
		temp_dict = {}
		temp_dict["measurement"] = "Watch_Time_" + str(days) + "_Days"
		response = requests.get(url + str(userlist[i]))
		response_json= json.loads(response.text)
		temp_dict["user"] = i
		temp_dict["data"] = {"total_time": response_json["response"]["data"][0]["total_time"], "total_plays": response_json["response"]["data"][0]["total_plays"]}
		watch_list.append(temp_dict)
	print(watch_list)

def get_user_list():
	"""
	Gets list of users
	"""
	user_list = {}
	url = f"http://10.0.0.126:8181/api/v2?apikey={api_key}&cmd=get_users"
	response = requests.get(url)
	response_json = json.loads(response.text)
	for i in response_json["response"]["data"]:
		user_list[i["friendly_name"]] = i["user_id"]
	return user_list


get_watched_time(10000, get_user_list())
get_watched_time(7, get_user_list())