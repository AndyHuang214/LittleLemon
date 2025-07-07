from django.test import TestCase
from LittleLemonAPI.models import MenuItem

class MenuItemTest(TestCase):
    def setUp(self):
        item1 = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        item2 = MenuItem.objects.create(title="IceCream2", price=200, inventory=200)
        item3 = MenuItem.objects.create(title="IceCream3", price=300, inventory=300)

    def test_getall(self):
        queryset =MenuItem.objects.all()
        self.assertEqual(queryset.count(), 3)
        self.assertEqual(str(queryset[0]), "IceCream : 80.00")