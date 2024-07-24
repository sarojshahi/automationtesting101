import requests
import json

#base url
base_url = "https://reqres.in/api"

#auth token
auth_token = "token ..... token value"

#define post request function
def post_request():
    url = base_url + "/users/"
    print(f"post request url:{url}")
    headers = {"Authorization": auth_token}
    data = {
        "name":"saroj shahi",
        "email":"saroj@gmail.com",
        "phone":"9818839688"
    }
    response = requests.post(headers=headers)
    assert response.status_code == 201
    json_data = response.json()
    json_str = json.dumps(json_data, indent=6)
    

