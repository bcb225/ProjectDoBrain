import requests
import json

class RestHandler:
    def __init__(self):
        self.base_url = 'https://dobrain-pro.firebaseio.com/drag_data/iOS/' #'https://dobrain-pro.firebaseio.com/drag_data/Android/'
    
    def get_json_by_person_id(self,person_id):
        target_url = self.base_url + person_id +'.json'
        resp = requests.get(url=target_url)
        json_text = resp.json()
        json_result = json.dumps(json_text)
        return json_text