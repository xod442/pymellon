#!/usr/bin/env python3
# coding=utf-8
# author: @netwookie.
# -*- coding: utf-8 -*-
"""
This is a test file that gets a token
"""
import urllib3
urllib3.disable_warnings()
import json
import requests

url = 'http://137.60.202.190/admin/launch?script=rh&template=login&action=login'

params = { 'f_user_id': 'admin',
         'f_password': 'admin'
        }
# don't know if we need to send JSON string or python dict
# params = json.dumps(params)

headers = {'Content-Type': 'application/x-www-form-urlencoded'}
r = requests.post(url, data=params, headers=headers)

print(r)
