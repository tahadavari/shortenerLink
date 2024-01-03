from unittest.mock import Mock

from django.test import TestCase

from shortener.models.link import Link


class LinkModelTest(TestCase):

    def setUp(self):
        self.mock_db = Mock(spec=Link.objects)
        self.link_instance = Link(original_link='https://www.example.com/', short_link='abc123')

    def test_original_link_max_length(self):
        self.mock_db.create.return_value = self.link_instance
        link = self.mock_db.create()
        max_length = link._meta.get_field('original_link').max_length
        self.assertEqual(max_length, 200)

    def test_short_link_unique(self):
        self.mock_db.create.return_value = self.link_instance
        link = self.mock_db.create()
        short_link_field = link._meta.get_field('short_link')
        self.assertTrue(short_link_field.unique)

    def test_str_representation(self):
        self.mock_db.create.return_value = self.link_instance
        link = self.mock_db.create()
        self.assertEqual(str(link), 'https://www.example.com/')

    def test_original_link_field_exists(self):
        fields = Link._meta.get_fields()
        field_names = [field.name for field in fields]
        self.assertIn('original_link', field_names)

    def test_short_link_field_type(self):
        field = Link._meta.get_field('short_link')
        self.assertEqual(field.get_internal_type(), 'CharField')
        self.assertEqual(field.max_length, 100)
        self.assertTrue(field.unique)
