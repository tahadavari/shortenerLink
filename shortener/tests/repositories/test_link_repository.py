from django.core.files.base import ContentFile
from django.test import TestCase
from unittest.mock import patch, Mock

from shortener.models.link import Link
from shortener.repositories.link_repository import LinkRepository


class TestLinkRepository(TestCase):

    def test_create_link_with_mock_db(self):
        original_link = 'https://www.example.com/'
        short_link = 'abc123'
        qr_binary = ContentFile(b'abc123')

        with patch('shortener.utils.shortener_link.ShortenerLink.short_link') as mock_shortener_link, \
                patch('shortener.utils.qr_creator.QrCreator.get_content_img') as mock_qr_creator:
            mock_shortener_link.return_value = short_link
            mock_qr_creator.return_value = qr_binary

            link_repository = LinkRepository()

            created_link = link_repository.create_link(original_link)

            self.assertIsInstance(created_link, Link)
            self.assertEqual(created_link.original_link, original_link)
            self.assertEqual(created_link.short_link, short_link)

            saved_links = Link.objects.all()
            self.assertEqual(saved_links.count(), 1)
            saved_link = saved_links.first()
            self.assertEqual(saved_link.original_link, original_link)
            self.assertEqual(saved_link.short_link, short_link)

            expected_filename = f'qr_{short_link}.png'
            self.assertTrue(saved_link.qr_code.name.endswith(expected_filename))

    def test_get_original_link(self):
        expected_original_link = 'http://example.com'
        short_link = 'http://example2.com'

        mock_instance = Link(original_link=expected_original_link, short_link=short_link)

        with patch('shortener.models.link.Link.objects.get') as mock_get:
            mock_get.return_value = mock_instance

            link_repository = LinkRepository()
            original_link = link_repository.get_original_link(short_link)

            self.assertEqual(original_link, expected_original_link)
