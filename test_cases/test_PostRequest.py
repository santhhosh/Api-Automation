import requests
import json
import jsonpath

from config.test_env_config import *
from logs.logger import *
from logs.logger import logclass
from Data.testdata import *


class TestPostRequest(logclass):

    def test_post_request_create(self):
        log = self.get_the_logs()
        log.info("Starting test_post_request_create")

        with open(post_request_data) as file:
            request_json = json.load(file)

        response = requests.post(Post_URL, json=request_json)

        # Validating response code
        """assert response.status_code == 201, f"Expected 201 but got {response.status_code}"
        print("Response of Post Method:", response)

        # Fetch header and content from response
        print("Content of Post Method:", response.content)
        print("Header of Post Method:", response.headers)

        # Parse response to JSON
        json_response = response.json()
        print("JSON Response:", json_response)

        # Pick id using json path from response
        
        id = jsonpath.jsonpath(json_response, 'id')
        if id:
            print("Id from the response:", id[0])
        else:
            print("ID not found in the response")

        log.info("Ending test_post_request_create")

   def test_post_request_register(self):
        log = self.get_the_logs()
        log.info("Starting test_post_request_register")

        with open(post_request_data1) as file:
            request_json = json.load(file)

        response = requests.post(Post_URL1, json=request_json)

        assert response.status_code == 200, f"Expected 200 but got {response.status_code}"
        print("Response of Post Method:", response)
        print("Content of Post Method:", response.content)
        print("Header of Post Method:", response.headers)

        json_response = response.json()
        print("JSON Response:", json_response)

        log.info("Ending test_post_request_register")

    def test_post_request_login(self):
        log = self.get_the_logs()
        log.info("Starting test_post_request_login")

        with open(post_request_data2) as file:
            request_json = json.load(file)

        response = requests.post(Post_URL2, json=request_json)

        assert response.status_code == 200, f"Expected 200 but got {response.status_code}"
        print("Response of Post Method:", response)
        print("Content of Post Method:", response.content)
        print("Header of Post Method:", response.headers)

        json_response = response.json()
        print("JSON Response:", json_response)

        log.info("Ending test_post_request_login")"""
