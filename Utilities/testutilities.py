from Data.testdata import *
import json
import requests


class useabileffiles:
 def test_file_uses(self,request_json):
  file = open(put_request_data)
  json_input = file.read()
  request_json = json.loads(json_input)

  def test_log_uses(self):
   log = self.get_the_logs()
   log.info("Starting test_post_request_create")
