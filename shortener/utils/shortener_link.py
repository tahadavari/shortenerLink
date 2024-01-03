from hashids import Hashids

from linkShortener import settings


class ShortenerLink:
    def __init__(self):
        self.salt = settings.HASHIDS_SALT
        self.min_length = settings.LINK_MIN_LENGTH

    def short_link(self, url):
        hashids = Hashids(url, min_length=self.min_length)
        return hashids.encode(1,2,3)
