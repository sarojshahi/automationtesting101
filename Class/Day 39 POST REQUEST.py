import requests
import json

#base url
base_url = "https://reqres.in/api"

#auth token
auth_token = "token .....token value"

#initiate post function
def post_request():
    url = base_url + "/users"