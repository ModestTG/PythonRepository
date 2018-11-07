#allows print() funtion to work in python2
from __future__ import print_function


ip_addr1 = '8.8.8.8'
print(ip_addr1)
try:
    ip_addr2 = raw_input("Enter an IP Address: ")
except NameError:
    ip_addr2 = input("Enter an IP Address: ")
print(ip_addr2)

