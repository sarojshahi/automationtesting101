import string

import requests
import json
import random


#function to generate random email
def generate_random_email():
    domain = "@gmail.com"
    random_string = "".join(random.choices(string.ascii_lowercase, k= 8)) + domain
    return random_string

email = generate_random_email()
print(email)

#base_url
base_url = "https://reqres.in/api"

#auth token
auth_token = "token .... token value"

#function to define put request
def put_request(user_id):
    url = base_url + "/users/{user_id}"
    print("put request: ", url)
    headers = {"Authorization": auth_token}
    data = {
        "name":"Radhey Shyam",
        "email": email,
        "job": "QA Learner"

    }
    response = requests.put(url, json=data, headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=5)
    print("PUT REQUEST:", json_str)

put_request(2)