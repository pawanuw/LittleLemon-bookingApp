from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from Restaurant.models import Menu
from Restaurant.serializers import MenuSerializer
from django.contrib.auth.models import User

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")

class MenuViewTest(TestCase):
    def setUp(self):
        self.menu1 = Menu.objects.create(title="Pizza", price=10.99, inventory=20)
        self.menu2 = Menu.objects.create(title="Burger", price=5.49, inventory=35)
        self.menu3 = Menu.objects.create(title="Salad", price=7.99, inventory=15)

        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_getall(self):
        response = self.client.get('/restaurant/menu/')

        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)