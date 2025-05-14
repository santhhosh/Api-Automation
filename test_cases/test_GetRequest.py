import requests
import json
import jsonpath
from config.test_env_config import *
from logs.logger import logclass


class TestGetRequest(logclass):

 def test_get_request_listuser(self):
  log = self.get_the_logs()
  log.info("Starting test_get_request_listuser")

  # Send GET request
  response = requests.get(Get_URL)
  log.info(f"GET response: {response}")

  # Validate response
  assert response.status_code == 200, f"Expected status 200 but got {response.status_code}"

  # Print response content and headers
  print("Content of GET method:", response.content)
  print("Header of GET method:", response.headers)

  # Parse response to JSON
  json_response = response.json()
  print("JSON response:", json_response)

  # Fetch value using jsonpath
  pages = jsonpath.jsonpath(json_response, 'total_pages')
  assert pages is not False and pages[0] == 5, "Expected total_pages to be 2"
  print("Total pages:", pages[0])

 def test_get_request_singleuser(self):
  log = self.get_the_logs()
  log.info("Starting test_get_request_singleuser")

  # Send GET request
  response = requests.get(Get_URL1)
  log.info(f"GET response: {response}")

  # Validate response
  assert response.status_code == 200, f"Expected status 200 but got {response.status_code}"

  # Print response content and headers
  print("Content of GET method (single user):", response.content)
  print("Header of GET method (single user):", response.headers)

  # Parse response to JSON
  json_response = response.json()
  print("JSON response (single user):", json_response)

  # Fetch value using jsonpath
  first_name = jsonpath.jsonpath(json_response, '$.data.first_name')
  if first_name:
   print("First name:", first_name[0])
  else:
   log.warning("First name not found in response")
