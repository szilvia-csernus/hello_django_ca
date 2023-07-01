from django.test import TestCase
from .models import Item


class TestViews(TestCase):

    def test_done_defaults_to_false(self):
        """Test Done Defaults to False"""
        item = Item.objects.create(name='Test Todo Item')
        self.assertFalse(item.done)

    def test_item_string_method_returns_name(self):
        """Test Item String Method Returns Name"""
        item = Item.objects.create(name='Test Todo Item')
        self.assertEqual(str(item), 'Test Todo Item')
