from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from app.models import *
from uuid import uuid1
import requests

class RedirectTestCase(TestCase):
    def setUp(self):
        slug = '12345678'
        target_url = 'http://facebook.com/'
        slug_obj = Redirect.objects.create(slug=slug)
        URLData.objects.create(slug=slug_obj, target_url=target_url)
    def test_redirection_works(self):
        target_url = URLData.objects.get(slug__slug='12345678').target_url
        response = requests.get(target_url)
        for resp in response.history:
            print(resp.url)
            self.assertEqual(resp.url, target_url)
            break
