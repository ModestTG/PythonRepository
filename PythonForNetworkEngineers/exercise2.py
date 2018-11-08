from __future__ import print_function, unicode_literals

try:
    ip_addr = raw_input("Enter an IP Address: ")
except NameError:
    ip_addr = input("Enter an IP Address: ")

octets = ip_addr.split(".")
print("\n")
print("{:^15}{:^15}{:^15}{:^15}".format("Octet1", "Octet2", "Octet3", "Octet4"))
print("-" * 60)
print("{:^15}{:^15}{:^15}{:^15}".format(*octets))
print("{:^15}{:^15}{:^15}{:^15}".format(format((int(octets[0])),"#010b"), format((int(octets[1])),"#010b"), format((int(octets[2])),"#010b"), format((int(octets[3])),"#010b"), ))
print("{:^15}{:^15}{:^15}{:^15}".format(hex(int(octets[0])), hex(int(octets[1])), hex(int(octets[2])), hex(int(octets[3]))))
print("-" * 60)
