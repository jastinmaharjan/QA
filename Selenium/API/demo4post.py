# post request

import requests
import json

# base url
base_url = "https://reqres.in/api"
# auth key:
auth_token="token ....token value"
# Post Request
def post_request():
    url=base_url+"/users/"
    print("Post url:"+url)
    headers={"Authorization":auth_token}
    data={
        "name":"Justin",
        "email":"justin@gmail.com",
        "job":"quality assurance"
    }
    response=requests.post(url,json=data,headers=headers)
    json_data=response.json()
    json_str=json.dumps(json_data,indent=4)
    print("Json Post request body:", json_str)
    user_id=json_data["id"]
    print("User Id===>",user_id)
    assert response.status_code==201
    assert "name" in json_data
    return user_id

user_id=post_request()





















