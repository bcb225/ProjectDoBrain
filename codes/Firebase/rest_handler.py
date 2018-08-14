import requests
import json

class RestHandler:
    def __init__(self):
        self.base_drag_data_url = 'https://dobrain-pro.firebaseio.com/drag_data/iOS/' #'https://dobrain-pro.firebaseio.com/drag_data/Android/'
        self.user_url = 'https://dobrain-pro.firebaseio.com/users/iOS/'
    def get_json_by_person_id(self,person_id):
        target_url = self.base_drag_data_url + person_id +'.json'
        resp = requests.get(url=target_url)
        json_text = resp.json()
        json_result = json.dumps(json_text)
        return json_text
    
    def get_json_of_person_id(self):
        target_url = self.user_url +'.json' +'?shallow=true'
        resp = requests.get(url=target_url)
        print(resp.text)
        json_text = resp.json()
        json_result = json.dumps(json_text)
        return json_result

