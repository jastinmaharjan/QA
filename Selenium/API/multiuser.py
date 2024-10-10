import requests
import json

# Base URL:
base_url = "https://reqres.in/api"
#Auth token:
auth_token = "token ...token value"

#POST Request
def post_request(user_names):
    url = base_url + "/users/"
    print("post url: " + url)
    headers = {"Authorization": auth_token}
    user_ids = []

    for name in user_names:
        data = {
            "name": name,
            "job": "qa"
        }
        response = requests.post(url, json=data, headers=headers)
        json_data = response.json()
        json_str = json.dumps(json_data, indent=4)
        print("json POST response body for", name, ":", json_str)
        user_id = json_data.get("id")
        if user_id:
            user_ids.append(user_id)
        assert response.status_code == 201
        assert "name" in json_data
        print(".......POST/Create USER IS SUCCESSFUL for", name, ".......")
        print(".......=====================.......")

    return user_ids
#user name example
user_names = ["Justin", "James","Roanldo","Ed"]
user_ids = post_request(user_names)
print("Created user IDs:", user_ids)
