import requests
import json

#base url
base_url = "https://reqres.in/api"

#auth token
auth_token = "token .... token value"

#define function for post request
def post_request():
    url = base_url + "/users/"
    print("post url:",url)
    headers = {"Authorization":auth_token}
    data = {
        "name" : "Rama Shanker",
        "email" : "ramashankar@gmail.com",
        "job" : "Fulki Chat Business"
    }
    response = requests.post(url, json=data, headers=headers)
    assert response.status_code == 201
    json_data = response.json()
    json_str = json.dumps(json_data, indent=5)
    print(f"POST USER REQUEST BODY:{json_str}")
    print(".............__________............")
    print(".............POST REQUEST SUCCESSFUL............")

post_request()
