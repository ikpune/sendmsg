from django.test import TestCase
from rest_framework.test import APIRequestFactory
import unittest

# Create your tests here.

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
    	factory = APIRequestFactory()
    	request = factory.post('/api/sendmsg/', {'msg': 'test message'})

if __name__ == '__main__':
    unittest.main()