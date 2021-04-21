#!/usr/bin/env python3
import requests
from hashlib import md5
import time

API = "https://api.wyzecam.com:8443"
USERNAME = "example@email.com"
_PASSWORD = b"yourpassword"
PASSWORD = md5(md5(_PASSWORD).hexdigest().encode()).hexdigest()

def current_milli_time():
    return int(round(time.time() * 1000))

def login():
    url = API + "/app/user/login"

    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "sc": "[sc-alphanumeric]",
        "sv": "[sv-alphanmueric]",
        "app_ver": "com.hualai___2.0.18",
        "ts": current_milli_time(),
        "access_token": "",
        "phone_id": "[phone-uuid4]",
        "user_name": USERNAME,
        "password": PASSWORD
    }

    print(payload)

    response = requests.post(url, headers=headers, json=payload)
    print(response.status_code)

    json_response = response.json()
    print(json_response)

    user_center_id = json_response['data']['user_center_id']
    access_token = json_response['data']['access_token']
    refresh_token = json_response['data']['refresh_token']

    return user_center_id, access_token, refresh_token
