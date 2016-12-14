from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import TextMessages

class AccountTests(APITestCase):
    def test_send_msg(self):
        """
        Ensure we can create a new account object.
        """
        url = 'http://localhost:8000/api/sendmsg'
        data = {'msg': 'Hello'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(TextMessages.objects.count(), 1)
        self.assertEqual(TextMessages.objects.get().text_message, 'Hello')