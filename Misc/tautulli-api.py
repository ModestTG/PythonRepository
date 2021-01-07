import requests
import json

api_key = "87d3d012d4324de4bee3bf20c31d8ec5"
users="get_users"
watch="get_user_watch_time_stats"
days=10000

url2 = f"http://10.0.0.126:8181/api/v2?apikey={api_key}&cmd={users}"
user_data = requests.get(url2)
user_parsed_data = json.loads(user_data.text)
# print(user_parsed_data)
# with open("response.json", "w") as f:
# 	f.write(json.dumps(user_data.json(), indent=4))
user_list = {}
for i in user_parsed_data["response"]["data"]:
	user_list[i["friendly_name"]] = i["user_id"]

# print(user_list)
for i in user_list:
	url1 = f"http://10.0.0.126:8181/api/v2?apikey={api_key}&cmd={watch}&query_days={days}&user_id={user_list[i]}"
	watch_data = requests.get(url1)
	watch_parsed_data = json.loads(watch_data.text)
	print(i)
	print(watch_parsed_data)
