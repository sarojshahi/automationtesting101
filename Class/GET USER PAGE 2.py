import requests
import json

#base url
base_url = "https://reqres.in/api"

#auth key
auth_token = "token .... token value"

#define pagination api request
def get_request(page):
    url = base_url+f"/users?page={page}"
    headers = {"Authorization":auth_token}if auth_token else {}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=6)
    print(f"get request body: {json_str}")

get_request(2)

