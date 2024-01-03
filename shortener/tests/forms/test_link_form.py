from django.test import TestCase

from shortener.forms.link_form import LinkForm


class TestLinkForm(TestCase):

    def test_valid_link(self):
        # اعتبارسنجی لینک معتبر
        form = LinkForm({'original_link': 'https://www.example.com/'})
        self.assertTrue(form.is_valid())  # فرم باید معتبر باشد

    def test_invalid_link(self):
        # اعتبارسنجی لینک نامعتبر
        form = LinkForm({'original_link': 'invalid_link'})
        self.assertFalse(form.is_valid())  # فرم باید نامعتبر باشد

    def test_blank_link(self):
        # بررسی ورودی خالی
        form = LinkForm({'original_link': ''})
        self.assertFalse(form.is_valid())  # فرم باید نامعتبر باشد

    def test_empty_data(self):
        # بررسی ارسال داده‌های خالی
        form = LinkForm({})
        self.assertFalse(form.is_valid())  # فرم باید نامعتبر باشد
