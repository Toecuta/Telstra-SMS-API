# coding: utf-8

"""
    Telstra SMS Messaging API

    The Telstra SMS Messaging API allows your applications to send and receive SMS text messages from Australia's leading network operator. It also allows your application to track the delivery status of both sent and received SMS messages. 

    OpenAPI spec version: 2.1.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.models.error import Error


class TestError(unittest.TestCase):
    """ Error unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testError(self):
        """
        Test Error
        """
        model = swagger_client.models.error.Error()


if __name__ == '__main__':
    unittest.main()
