from io import BytesIO

import qrcode
from django.core.files.base import ContentFile


class QrCreator:
    def __init__(self, url):
        self.url = url
        self.img = self._create_img()

    def _create_img(self):
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(self.url)
        qr.make(fit=True)
        return qr.make_image(fill='black', back_color='white')

    def get_content_img(self):
        buffer = BytesIO()
        self.img.save(buffer)
        file_buffer = ContentFile(buffer.getvalue())
        return file_buffer
