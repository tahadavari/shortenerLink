from linkShortener import settings
from shortener.models.link import Link
from shortener.utils.qr_creator import QrCreator
from shortener.utils.shortener_link import ShortenerLink


class LinkRepository:
    def create_link(self, original_link):
        shortener_link = ShortenerLink()
        short_link = shortener_link.short_link(original_link)

        qr = QrCreator(settings.BASE_URL + short_link)
        filename = f'qr_{short_link}.png'

        link = Link.objects.create(original_link=original_link, short_link=short_link)
        link.qr_code.save(filename, qr.get_content_img())
        return link

    def get_original_link(self, short_link):
        return Link.objects.get(short_link=short_link).original_link
