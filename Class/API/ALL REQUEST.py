import random
import string

import requests
import json

#base_url
base_url = "https://reqres.in/api"

#auth token
auth_token = "token .... token value"

#generate random email function
def generate_random_email():
    domain = "@gmail.com"
    email_length = 10
    random_string = "".join(random.choice(string.ascii_lowercase) for _ in range (email_length))
    email = random_string + domain
    return email

#generate random phone function
def generate_random_phone():
    random_string = "98"+"".join(random.choices(string.digits,k =8))
    return random_string


#GET REQUEST
def  get_request():
    url = base_url + "/users/"
    print(f"GET REQUEST URL: {url}")
    headers = {"Authorization":auth_token}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=6)
    print(f"JSON GET REQUEST BODY:{json_str}")
    print("...........=======................")
    print("..................................")

#calling the get request
get_request()

#POST REQUEST

def post_request():
    url= base_url + "/users"
    print(f"POST REQUEST URL:{url}")
    headers = {"Authorization":auth_token}
    data = {
        "name":"ram",
        "email": generate_random_email(),
        "phone": generate_random_phone()
    }
    response = requests.post(url,json=data, headers = headers)
    assert response.status_code == 201
    json_data = response.json()
    json_str = json.dumps(json_data,indent=6)
    print(f"JSON POST REQUEST BODY:{json_str}")
    print("YOUR POST REQUEST IS COMPLETE")
    print("...........=======................")
    print("..................................")
#calling the POST function
post_request()

#PUT REQUEST
def put_request(user_id):
    url = base_url + f"/users/{user_id}"
    print(f"PUT REQUEST URL: {url}")
    headers = {"Authorization": auth_token}
    data = {
        "name":"shyam",
        "email": generate_random_email(),
        "phone": generate_random_phone()
    }
    response = requests.put(url, json=data, headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print(f"PUT REQUEST BODY:{json_str}")
    print("PUT REQUEST IS SUCCESSFUL")
    print("...........=======................")
    print("..................................")
#calling the PUT function
put_request(2)

#DELETE USER FUNCTION
def delete_request(user_id):
    url = base_url + f"/users/{user_id}"
    print(f"DELETE USER REQUEST URL: {url}")
    headers = {"Authorization": auth_token}
    response = requests.delete(url, headers=headers)
    assert response.status_code == 204
    print("DELETE REQUEST IS SUCCESSFUL")
    print("...........=======................")
    print("..................................")

#calling the delete function
delete_request(3)

