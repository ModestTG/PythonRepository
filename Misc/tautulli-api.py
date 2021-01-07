import requests
import json

api_key = ""
with open("api.txt", "r") as f:
	api_key = str.strip(f.read())

# user_data = requests.get(url2)
# user_parsed_data = json.loads(user_data.text)
# # print(user_parsed_data)
# # with open("response.json", "w") as f:
# # 	f.write(json.dumps(user_data.json(), indent=4))
# user_list = {}
# for i in user_parsed_data["response"]["data"]:
# 	user_list[i["friendly_name"]] = i["user_id"]

# # print(user_list)
# for i in user_list:
# 	url1 = f"http://10.0.0.126:8181/api/v2?apikey={api_key}&cmd={watch}&query_days={days}&user_id={user_list[i]}"
# 	watch_data = requests.get(url1)
# 	watch_parsed_data = json.loads(watch_data.text)
# 	print(i)
# 	print(watch_parsed_data)

	# for i in sorted_values:
	# 	for j in user_list.keys():
	# 		if user_list[j] == i:
	# 			sorted_dict[j] = user_list[j]
	# 			break
	
def get_watched_time(days, userlist):
	watch_list = []
	url = f"http://10.0.0.126:8181/api/v2?apikey={api_key}&cmd=get_user_watch_time_stats&query_days={days}&user_id="
	for i in userlist:
		temp_dict = {}
		temp_dict["measurement"] = "Watch_Time_" + str(days) + "_Days"
		response = requests.get(url + str(userlist[i]))
		response_json= json.loads(response.text)
		# formatted_response_json = json.dumps(response_json, indent=4)
		# print(formatted_response_json)
		temp_dict["user"] = i
		temp_dict["data"] = {"total_time": response_json["response"]["data"][0]["total_time"], "total_plays": response_json["response"]["data"][0]["total_plays"]}
		watch_list.append(temp_dict)
	print(json.dumps(watch_list, indent=4))


def get_user_list():
	user_list = {}
	url = f"http://10.0.0.126:8181/api/v2?apikey={api_key}&cmd=get_users"
	response = requests.get(url)
	response_json = json.loads(response.text)
	# formatted_user_list = json.dumps(response_json, indent=4)
	# print(formatted_user_list)
	for i in response_json["response"]["data"]:
		user_list[i["friendly_name"]] = i["user_id"]
	# print(user_list)
	return user_list


# get_user_list()
get_watched_time(10000, get_user_list())
get_watched_time(7, get_user_list())
