import requests
import json

#base url
base_url = "https://reqres.in/api"

#auth token
auth_token = "token ........ token value"

#define get request function
def get_request():
    url = base_url + "/users"
    print(f"Get user request: {url}")
    headers = {"Authorization": auth_token}
    response = requests.get(url,headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=6)
    print(f"GET USER REQUEST: {json_str}")
    print(".........USER REQUEST IS DONE...............")
    print("............................................")

#defining function
get_request()