from django.test import TestCase

from shortener.forms.link_form import LinkForm


class TestLinkForm(TestCase):

    def test_valid_link(self):
        form = LinkForm({'original_link': 'https://www.example.com/'})
        self.assertTrue(form.is_valid())

    def test_invalid_link(self):
        form = LinkForm({'original_link': 'invalid_link'})
        self.assertFalse(form.is_valid())

    def test_blank_link(self):
        form = LinkForm({'original_link': ''})
        self.assertFalse(form.is_valid())  

    def test_empty_data(self):
        form = LinkForm({})
        self.assertTrue(form.is_valid())
