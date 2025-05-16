import json
import requests
import jsonpath
from config.test_env_config import *
from Data.testdata import *
from logs.logger import logclass

class TestPatchRequest(logclass):

 def test_patch_request_update(self):
  log = self.get_the_logs()
  log.info("Starting test_Patch_request")
  file = open(patch_request_data1)
  json_input = file.read()
  request_json = json.loads(json_input)

 #patch request with json input body
  response = requests.patch(Patch_URL1,request_json)

 #validating response code
  """assert response.status_code ==200
  print("Response of patch Method:",response)

 #fetch header and content from response

  print("Content of patch Method:",response.content)
  print("header of patch Method:",response.headers)

 #parse response to json format
  json_response = json.loads(response.text)
  print("json_response:",json_response)
  log.info("Ending test_patch_request")"""






