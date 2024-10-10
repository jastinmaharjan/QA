# delete request:

import requests
import json

# base url
base_url = "https://reqres.in/api"
# auth key:
auth_token="token ....token value"

# delete request
def delete_request(user_id):
    url=base_url +f"/users/{user_id}"
    print("Delete url:"+url)
    headers={"Authorization":auth_token}
    response=requests.delete(url,headers=headers)
    assert response.status_code==204
    print("=====user is successfully deleted=====")

delete_request(4)
