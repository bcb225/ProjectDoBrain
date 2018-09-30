import requests
import json

class RestHandler:
    def __init__(self, mobile_os):
        self.base_drag_data_url = 'https://dobrain-pro.firebaseio.com/drag_data/{}/'.format(mobile_os) #'https://dobrain-pro.firebaseio.com/drag_data/Android/'
        self.base_lab_data_url = 'https://dobrain-pro.firebaseio.com/kids_lab_data/{}/'.format(mobile_os)
        self.user_url = 'https://dobrain-pro.firebaseio.com/users/{}/'.format(mobile_os)
        self.lesson_bucket_url ='https://dobrain-pro.firebaseio.com/lessonly_report_data_bucket/'
        self.survey_url = 'https://dobrain-pro.firebaseio.com/report_survey_data/{}/'.format(mobile_os)
    def get_json_by_person_id(self,person_id):
        target_url = self.base_drag_data_url + person_id +'.json'
        resp = requests.get(url=target_url)
        json_result = resp.json()
        return json_result
    
    def get_json_of_person_id(self):
        target_url = self.user_url +'.json' +'?shallow=true'
        resp = requests.get(url=target_url)
        json_result = resp.json()
        json_text = json.dumps(json_result)
        print(json_text)
        return json_text
    
    def get_user_data_by_person_id(self, person_id):
        target_url = self.user_url + person_id +'.json'
        resp = requests.get(url = target_url)
        json_result = resp.json()
        json_text = json.dumps(json_result)
        return json_text
    
    def get_lab_data_by_person_id(self, person_id):
        target_url = self.base_lab_data_url + person_id + '.json'
        resp = requests.get(url=target_url)
        json_result = resp.json()
        return json_result

    def get_lesson_bucket_data_by_index(self,index):
        target_url = self.lesson_bucket_url+str(index)+'.json'
        resp = requests.get(url=target_url)
        json_result = resp.json()
        return json_result

    def get_survey_data(self):
        target_url = self.survey_url + '.json'
        resp = requests.get(url = target_url)
        json_result = resp.json()
        return json_result