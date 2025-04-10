import json
import requests
import jsonpath
from config.test_env_config import *
from Data.testdata import *
from logs.logger import logclass


class TestPostRequest(logclass):
 def test_post_request_create(self):
  log = self.get_the_logs()
  log.info("Starting test_post_request_create")
  file = open(post_request_data)
  json_input = file.read()
  request_json = json.loads(json_input)

 #post request with json input body
  response = requests.post(Post_URL,request_json)

 #validating response code
  assert response.status_code ==201
  print("Response of Post Method:",response)

 #fetch header and content from response

  print("Content of Post Method:",response.content)
  print("header of Post Method:",response.headers)

 #parse response to json format
  json_response = json.loads(response.text)
  print("json_response:",json_response)

 #pick id using json path from response
  id = jsonpath.jsonpath(json_response,'id')
  print("Id from the response:",id[0])

 def test_post_request_register(self):
  log = self.get_the_logs()
  log.info("Starting test_post_request_register")
  file = open(post_request_data1)
  json_input = file.read()
  request_json = json.loads(json_input)

 #post request with json input body
  response = requests.post(Post_URL1,request_json)

 #validating response code
  assert response.status_code ==200
  print("Response of Post Method:",response)

 #fetch header and content from response

  print("Content of Post Method:",response.content)
  print("header of Post Method:",response.headers)

 #parse response to json format
  json_response = json.loads(response.text)
  print("json_response:",json_response)

 def test_post_request_login(self):
  log = self.get_the_logs()
  log.info("Starting test_post_request_login")
  file = open(post_request_data2)
  json_input = file.read()
  request_json = json.loads(json_input)

 #post request with json input body
  response = requests.post(Post_URL2,request_json)

 #validating response code
  assert response.status_code ==200
  print("Response of Post Method:",response)

 #fetch header and content from response

  print("Content of Post Method:",response.content)
  print("header of Post Method:",response.headers)

 #parse response to json format
  json_response = json.loads(response.text)
  print("json_response:",json_response)
  log.info("Ending test_post_request")


