import json
import sys
json_string = open("D:\AllSetsArray.json", encoding="utf8", errors='ignore')
parsed_json = json.load(json_string)
print(parsed_json["name"])
