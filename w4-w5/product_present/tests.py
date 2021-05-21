from django.test import TestCase, Client
from django.urls import reverse

from .models import HandProduct

# Model Test #


class HandProductModelTest(TestCase):
    def setUp(self) -> None:
        self.product = HandProduct(name="ru farshi")

    def test_hand_product_name_label(self):
        name = self.product._meta.get_field('name').verbose_name
        self.assertEqual(name, 'name')

    def test_hand_product_name_max_length(self):
        name_max_length = self.product._meta.get_field('name').max_length
        self.assertEqual(name_max_length, 255)


# view test #

class HandProductViewTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_url_hand_product_detail(self):
        url = reverse('hand-product-detail', kwargs={"slug":self.product.slug})
        self.assertEqual(url, f'/product_present/handproduct/{self.product.slug}/')

    def test_hand_product_detail(self):
        response = self.client.get(reverse('hand-product-detail', kwargs={"slug":"hello"}))
        print(response.status_code)