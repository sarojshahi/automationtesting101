import requests
import json

#base url
base_url = "https://reqres.in/api"

#auth token
auth_token = "token .... token value"

#multi user post function
def post_request(usernames):
    url = base_url+"/users/"
    print(f"post request url : {url}")
    headers = {"Authorization":auth_token}
    user_ids = []

    for name in usernames:
        data = {
            "name": name,
            "job": "QA Learner"
        }
        response = requests.post(url, json=data, headers=headers)
        json_data = response.json()
        json_str = json.dumps(json_data, indent=4)
        print(f"Json Data post body:{name}:{json_str}")
        user_id = json_data.get("id")
        if user_id:
            user_ids.append(user_id)
            assert response.status_code == 201
            assert "name" in json_data

    return user_ids

#example of usernames
usernames = ["qwe","rty","uio","asd","zxc","fgh"]
user_ids = post_request(usernames)
print(f"User Name Successfully printed for {usernames}")