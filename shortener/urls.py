from django.urls import path

from shortener.views import ShortenerLinkView, RedirectShortLink

urlpatterns = [
    path('', ShortenerLinkView.as_view(), name='shorten_link'),
    path('l/<slug:short_link>/', RedirectShortLink.as_view(), name='shortened_link'),
]
