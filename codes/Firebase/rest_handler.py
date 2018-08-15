import requests
import json

class RestHandler:
    def __init__(self):
        self.base_drag_data_url = 'https://dobrain-pro.firebaseio.com/drag_data/iOS/' #'https://dobrain-pro.firebaseio.com/drag_data/Android/'
        self.user_url_iOS = 'https://dobrain-pro.firebaseio.com/users/iOS/'
    def get_json_by_person_id(self,person_id):
        target_url = self.base_drag_data_url + person_id +'.json'
        resp = requests.get(url=target_url)
        json_result = resp.json()
        return json_result
    
    def get_json_of_person_id(self):
        target_url = self.user_url_iOS +'.json' +'?shallow=true'
        resp = requests.get(url=target_url)
        json_result = resp.json()
        json_text = json.dumps(json_result)
        return json_text
    
    def get_user_data_by_person_id(self, person_id):
        target_url = self.user_url_iOS + person_id +'.json'
        resp = requests.get(url = target_url)
        json_result = resp.json()
        json_text = json.dumps(json_result)
        return json_text

