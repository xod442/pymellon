import requests
import json
import urllib3
urllib3.disable_warnings()

#.
class Auth(object):

    def __init__(
            self, host,
            username, password):
        """
        Using Sessions to get key
        """
        self.username = username
        self.password = password
        self.host = host

        params = {
            'script': 'rh',
            'template': 'json-request',
            'action': 'json-login',
        }

        data = {
          'username': self.username,
          'password': self.password
        }

        data= json.dumps(data)

        response = s.post(url, params=params, headers=headers, data=data)
        client_dict = s.cookies.get_dict()
        session_key = client_dict['session']
        key = 'session=' + session_key

        self.key = key
