import requests
import time
import aes
import json


HEADERS = {
    'content-type':'application/json',
}


class SasAPI():

    def __init__(self, url):
        self.base_url = url + '/admin/api/index.php/api/'
        self.session = requests.Session()
        self.session.headers = HEADERS


    # the payload must be <str> jsonified
    def post (self, token, route, payload):
        url = self.base_url + route
        self.session.headers['Authorization'] = f'Bearer {token}'
        data  = {
            'payload': payload
        }
        req = self.session.post(url, json=data)
        if req.status_code == 200:
            return req.json()
        return req.status_code

    def put (self, token, route, payload):
        url = self.base_url + route
        self.session.headers['Authorization'] = f'Bearer {token}'
        data  = {
            'payload': payload
        }
        req = self.session.put(url, json=data)
        if req.status_code == 200:
            return req.json()
        return req.status_code


    def get (self, token, route):
        url = self.base_url + route
        self.session.headers['Authorization'] = f'Bearer {token}'
        
        req = self.session.get(url)
        if req.status_code == 200:
            return req.json()
        return req.status_code

    def delete (self, token, route):
        url = self.base_url + route
        self.session.headers['Authorization'] = f'Bearer {token}'
        
        req = self.session.delete(url)
        if req.status_code == 200:
            return req.json()
        return req.status_code
    
    def login(self, username, password):
        route = 'login'
        payload = aes.encrypt(json.dumps({
            'username': username,
            'password': password
        }))
        data = {
            'payload': payload,
        }
        login_url = self.base_url + route
        response = self.session.post(login_url, json=data)
        if response.status_code != 200:
            return {'status': response.status_code}
            
        return json.loads(response.content)['token']


    def details(self, token):
            route = 'user'
            user_url = self.base_url + route
            self.session.headers['Authorization'] = f'Bearer {token}'
            response = self.session.get(user_url)
            return response.json()
