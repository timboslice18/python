import requests
import json


url = "https://172.17.71.202/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/policy/accesspolicies"


username = "apiUser"
password = "APIPassword123"
payload  = {}
headers = {
  'X-auth-access-token': 'dbcfe1a9-9aa8-429d-8ecb-d626a569235a',
  'X-auth-refresh-token': '989cbae3-e54c-4e32-9372-f8db5d7bbe57',
  'Content-Type': 'application/json',
  'Authorization': 'Basic YXBpVXNlcjpBUElQYXNzd29yZDEyMw=='
}

response = requests.request("GET", url, headers=headers, data = payload, auth=requests.auth.HTTPBasicAuth(username,password), verify=False)

json_data = json.loads(response.text)

#allows you to pretty print json data
#json_formatted_str = json.dumps(json_data, indent=2)

json_items = json_data["items"]

json_items_formatted_str = json.dumps(json_items, indent=2)

#print(json_items_formatted_str)
#print(json_items[2])
for item in json_items:
  if item["name"] == "test":
    print(item["name"])
    print(item["id"])





#print(json_items_formatted_str)
#print(json_items)
#print(type(json_items))

#it = iter(json_items)
#res_dct = dict(zip(it, it))
#print(type(res_dct))


"""
for key in json_data:
  for inner_dict in key["items"]:
    print(inner_dict)


for d in json_data['items']:
"""

