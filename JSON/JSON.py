from __future__ import print_function
import json
import sys
with open(r"D:\AllSetsArray.json", encoding="utf8", errors='ignore') as json_string:
    parsed_json = json.load(json_string)

print(parsed_json["name"])
