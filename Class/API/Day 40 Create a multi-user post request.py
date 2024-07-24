import requests
import json

#base url
base_url = "https://reqres.in/api"

#auth token
auth_token = "token ........ token value"

#post request
def post_request(user_names):
    url = base_url +"/users/"
    print(f"post url:{url}")
    headers = {"Authorization": auth_token }
    user_ids = []

    for name in user_names:
        data = {
            "name": name,
            "job":"QA Learner"
        }

        response = requests.post(url, json=data, headers=headers)
        json_data = response.json()
        json_str = json.dumps(json_data, indent=4)
        print(f"Json Data post response:{name}:{json_str}")
        user_id = json_data.get("id")
        if user_id:
            user_ids.append(user_id)
        assert response.status_code ==201
        assert "name" in json_data
        print("............ Post/user is created succesfully...........")

    return user_ids

user_name = ["saroj", "Sabal", "Proush", "Gaurav", "Brizendra"]
user_ids = post_request(user_name)
print(f"Created User Id: {user_ids}")
