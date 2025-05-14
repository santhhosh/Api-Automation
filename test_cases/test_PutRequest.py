import json
import requests
import jsonpath
from config.test_env_config import *
from Data.testdata import *
from logs.logger import logclass
from Utilities.testutilities import *

class TestPutRequest(logclass):
 def test_put_request_update(self):
  #log = self.get_the_logs()
  #log.info("Starting test_put_request_update")
  #file = open(put_request_data)
  #json_input = file.read()
  #request_json = json.loads(json_input)

 #put request with json input body
  response = requests.put(Put_URL1,request_json)

 #validating response code
  assert response.status_code ==201
  print("Response of Put Method:",response)

 #fetch header and content from response

  print("Content of Put Method:",response.content)
  print("header of Put Method:",response.headers)

 #parse response to json format
  json_response = json.loads(response.text)
  print("json_response:",json_response)

 #pick id using json path from response
  job = jsonpath.jsonpath(json_response,'job')
  print("job from the response:",job)





