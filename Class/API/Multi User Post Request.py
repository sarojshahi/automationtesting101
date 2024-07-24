import requests
import json

#base url
base_url = "https://reqres.in/api"

#auth token
auth_token = "token .... token value"


#define function for multi user post request
def post_request(usernames):
    url = base_url+"/users/"
    print(f"post request:{url}")
    headers = {"Authorization":auth_token}
    user_ids = []

    for name in usernames:
        data = {
            "name": name,
            "job": "QA Learner"
        }
        response = requests.post(url, json=data, headers=headers)
        json_data = response.json()
        json_str = json.dumps(json_data, indent =4)
        print(f"post reqeust")