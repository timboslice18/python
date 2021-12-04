import urllib
import re
import netaddr

# Range of IP Addresses that we see connections from.
ip_list = ['10.11.117.137', '10.11.122.20', '10.24.33.21', '10.11.122.22']

# List of IP Subnets that members of IP list should not be from.
banned_subnets = ['10.11.117.0/24', '10.24.33.0/24']

# Using banned_subnets as our master list see if any of the ip_list addresses are present
# If they are present print the ip address

new_list = [str(ip) for ip in netaddr.IPSet(ip_list) & (netaddr.IPSet(banned_subnets))]
print new_list

