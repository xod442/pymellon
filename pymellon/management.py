#!/usr/bin/env python3
# coding=utf-8
# author: @netwookie.
# -*- coding: utf-8 -*-
"""
Command processor
"""
import urllib3
urllib3.disable_warnings()
from pymellon.auth import Auth
import json
import requests

class Management(Auth):

    def __init__(
            self, host,
            username, password
            ):

        Auth.__init__(self, host, username, password)

        self.headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'cookie': self.key
        }

        self.params = {
            'script': 'json',
        }

        self.endpoint ='https://' + host +  '/admin/launch'


    def get_running_config():

        data = {"cmd": "show running"}
        data= json.dumps(data)

    	response = requests.get(self.endpoint, headers=self.headers, data=self.data, verify=False)

    	return response.json()
