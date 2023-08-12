from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from swags.models import Swag

class SwagAPITestCase(TestCase):
    def setUp(self):
        self.swag= Swag.objects.create(name='Test Swag', price=21.99)
        self.swag_list_url = reverse('swags:swag-list')
        self.swag_detail_url = reverse('swags:swag-detail', args=[self.swag.pk])

    def test_get_all_swag(self):
        response = self.client.get(self.swag_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_swag(self):
        response = self.client.get(self.swag_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_swag(self):
        data = {'name': 'New Swag', 'price': 45.99}
        response = self.client.post(self.swag_list_url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_update_swag(self):
        data = {'name': 'Updated Swag', 'price': 65.99}
        response = self.client.put(self.swag_list_url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_delete_swag(self):
        response = self.client.delete(self.swag_list_url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)