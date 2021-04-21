#!/usr/bin/env python3
import requests
import time
import login
import json

API = "https://api.wyzecam.com:8443"

user_center_id, access_token, refresh_token = login.login()

def current_milli_time():
    return int(round(time.time() * 1000))

def get_object_list(access_token, refresh_token):
    url = API + "/app/v2/home_page/get_object_list"

    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "sc": "[sc-alphanumeric]",
        "sv": "[sv-alphanmueric]",
        "app_ver": "com.hualai___2.0.18",
        "ts": current_milli_time(),
        "phone_id": "[phone-uuid4]",
        "access_token": access_token,
        "refresh_token": refresh_token
    }

    print(payload)

    response = requests.post(url, headers=headers, json=payload)

    print(response.status_code)
    json_response = response.json()

    json_formatted_str = json.dumps(json_response, indent=2)
    print(json_formatted_str)

if __name__ == "__main__":
    get_object_list(access_token, refresh_token)
