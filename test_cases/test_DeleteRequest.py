import requests
import json
import jsonpath
from config.test_env_config import *
from logs.logger import *
from logs.logger import logclass

class TestDeleteRequest(logclass):
 def test_delete_request_delete(self):
  #delete request
   log = self.get_the_logs()
   log.info("Starting test_Delete_request")
   response = requests.delete(Delete_URL1)

  #validate response
   print("Response of delete Method:",response)
   assert response.status_code ==204

  # display content and response of response
   print("Content of delete Method:",response.content)

   log.info("Ending test_Delete_request")


