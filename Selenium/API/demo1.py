# get request:
import requests
import json

# base url
base_url = "https://reqres.in/api"

# auth key:
auth_token="token ....token value"

def get_request():
    url=base_url +"/users/"
    print("get url:"+url)
    headers={"Authorization":auth_token}
    response= requests.get(url,headers=headers)
    assert  response.status_code ==200
    json_date=response.json()
    json_str=json.dumps(json_date,indent=4)
    print("json Get response Body",json_str)
    print("====Get method is done successfully=====")

# call the function
get_request()