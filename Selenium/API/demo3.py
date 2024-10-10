# get request/error handling:
import requests
import json

# base url
base_url = "https://reqres.in/api"   #correct link
# base_url = "https://reqres.in//.api"

# auth key:
auth_token="token ....token value"

def get_request(page):
    url=f"{base_url}/users?page={page}"
    print(f"Get Url:{url}")
    headers={"Authorization":auth_token} if auth_token else ()

    try:


         response= requests.get(url,headers=headers)
         assert  response.status_code ==200
         json_date=response.json()
         json_str=json.dumps(json_date,indent=4)
         print("json Get response Body",json_str)
    except requests.exceptions.HTTPError as http_err:
        print(f"Http error occured: {http_err}")

    except Exception as err:
        print(f"other error occured {err}")
    else:

         print("====Get method is done successfully=====")

# call the function
get_request(2)


