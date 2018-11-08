from __future__ import print_function, unicode_literals
import time


try:
    date_time = raw_input("Input your Date (MM/DD/YYYY hh:mm:ss): ")
except NameError:
    date_time = input("Input your Date (MM/DD/YYYY hh:mm:ss): ")

date_time_dmy = date_time.split(" ")[0].split("/")
date_time_hms = date_time.split(" ")[1].split(":")
print(f"{date_time_dmy} {date_time_hms}")

epochTime = time.mktime()
print(epochTime)
# epochTime = time.gmtime(1541707494)
# print(epochTime)