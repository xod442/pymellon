'''
                     _ _
  _ __ _  _ _ __  ___| | |___ _ _
 | '_ \ || | '  \/ -_) | / _ \ ' \
 | .__/\_, |_|_|_\___|_|_\___/_||_|
 |_|   |__/

A python binind for Mellanox ONX ethernet switches

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#  http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# __author__ = "@netwookie"
# __credits__ = ["Rick Kauffman"]
# __license__ = "Apache2.0"
# __maintainer__ = "Rick Kauffman"
# __email__ = "rick@rickkauffman.com"

'''

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

        response = s.post(url,params=params,headers=headers,data=data)
        client_dict = s.cookies.get_dict()
        session_key = client_dict['session']
        key = 'session=' + session_key

        self.key = key