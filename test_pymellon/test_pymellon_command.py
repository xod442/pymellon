# -*- coding: utf-8 -*-
"""
Module for testing the functions in pypheus.logs.
"""

import os
import vcr
from unittest import TestCase
from unittest import mock
from nose.plugins.skip import SkipTest
import urllib3
urllib3.disable_warnings()
import json
import requests

from pymellon.command import Command
from pymellon.management import Management
from pymellon.ports import Ports

host = os.environ['HOST']
username = os.environ['USERNAME']
password = os.environ['PASSWORD']

logs = Ports(host,username,password)

SKIPTEST=True

#TODO TAKE OUT HARDCODED DATA LATER
my_vcr = vcr.VCR(
    serializer='json',
    cassette_library_dir='./test_pymellon/fixtures/cassettes',
    record_mode='new_episodes',
    match_on=['uri', 'method'],
)

class Ports(TestCase):
    """
    Test Case for pypheus.network get_all_logs function
    """
    @vcr.use_cassette(cassette_library_dir='./test_pypheus/fixtures/cassettes')

    def test_get_all_logs(self):
        """
        Simple test to return all logs.
        :return:
        """
        test_logs = logs.get_all_logs()
        self.assertIs(type(test_logs['data']), list)
        self.assertIs(type(test_logs['data'][0]), dict)
