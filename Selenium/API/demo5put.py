# put request

import requests
import json
import random
import string

# base url
base_url = "https://reqres.in/api"
# auth key:
auth_token="token ....token value"

# get the random generate email
def generate_random_email():
    domain="gmail.com"
    email_length=5
    random_string=''.join(random.choice(string.ascii_lowercase) for _ in range(email_length))
    email=random_string +"@" +domain
    return email

# put function
def put_reqest(user_id):
    url=base_url +f"/users/{user_id}"
    print("Put url:"+url)
    headers={"Authorization":auth_token}
    data={
        "Name":"Justin",
        "email":generate_random_email(),
        "phone_number":"986159",
        "job":"quality assurance"
    }
    response = requests.put(url, json=data, headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("Json Put request body{page}", json_str)
    print("====Put method is done successfully====")

# call the function
put_reqest(86)
























