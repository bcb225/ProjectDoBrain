from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession
import google.auth
import requests

class FirebaseConnector:
    def __init__(self,key_path):
        self.scopes = [
                  "https://www.googleapis.com/auth/userinfo.email",
                  "https://www.googleapis.com/auth/firebase.database"
                ] 

        # Authenticate a credential with the service account
        self.credentials = service_account.Credentials.from_service_account_file(
            key_path, scopes=self.scopes)

        self.drag_data_ios_base_url = "https://dobrain-pro.firebaseio.com/drag_data/iOS"

    def get_drag_data_by_person_id(self,person_id):
        print (self.credentials)
        # Use the credentials object to authenticate a Requests session.
        authed_session = AuthorizedSession(self.credentials)
        target_url = self.drag_data_ios_base_url + '/' +person_id + '.json'
        print(target_url)
        response = authed_session.get(target_url)
        return response
    
    def get_access_token(self):
        request = google.auth.transport.requests.Request()
        self.credentials.refresh(request)
        self.access_token = self.credentials.token
        return self.access_token

    def get_drag_data_by_person_id_with_access_token(self, person_id):
        target_url = self.drag_data_ios_base_url + '/' +person_id + '.json?access_token=' + self.access_token
        print(target_url)
        resp = requests.get(url=target_url)
        return resp
#        curl "https://<DATABASE_NAME>.firebaseio.com/users/ada/name.json?access_token=<ACCESS_TOKEN>"