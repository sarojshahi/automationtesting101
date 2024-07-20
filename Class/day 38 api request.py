import requests
import json

#base url
base_url = "https://reqres.in/api"

#auth token
auth_token = "token ... token value"

#define get function
def get_request(page):
    url = base_url + f"/users?page={page}"
    headers = {"Authorization": auth_token}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=6)
    print(f"The Get Request body: {json_str}")
    print("THE GET REQUEST IS SUCCESSFUL!!!")
    print("................................")

get_request(2)


#######################################################################




import requests
import json

#base url
base_url = "https://reqres.in/api"

#auth token
auth_token = "token ... token value"

#define get function
def get_request():
    url = base_url + f"/users/"
    headers = {"Authorization": auth_token}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=6)
    print(f"The Get Request body: {json_str}")
    print("THE GET REQUEST IS SUCCESSFUL!!!")
    print("................................")

get_request(2)

