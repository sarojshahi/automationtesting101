import requests
import json

#set auth token
auth_token = "token .... token value"

#base url
base_url = "https://reqres.in/api"

#define function for delete request
def delete_request(user_id):
    url = base_url + f"/api/{user_id}"
    print("DELETE USER URL: ", url)
    headers = {"Authorization": auth_token}
    response = requests.delete(url, headers=headers)
    assert response.status_code == 204
    print("THE USER HAS BEEN DELETED")
    print("...........========...........")

delete_request(21)

