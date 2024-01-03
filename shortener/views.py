from django.shortcuts import render, redirect
from django.views import View

from linkShortener import settings
from .forms.link_form import LinkForm
from .repositories.link_repository import LinkRepository


class ShortenerLinkView(View):
    template_home_page = 'home.html'
    template_short_link_page = 'short-link.html'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.link_repository = LinkRepository()

    def get(self, request):
        form = LinkForm()
        return render(request, self.template_home_page, {'form': form})

    def post(self, request):
        form = LinkForm(request.POST)
        if form.is_valid():
            original_link = form.cleaned_data['original_link']
            link = self.link_repository.create_link(original_link)
            context = {
                'link': settings.BASE_URL + link.short_link,
                'qr_code': link.qr_code.url
            }
            return render(request, self.template_short_link_page, context)

        return render(request, self.template_home_page, {'form': form})


class RedirectShortLink(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.link_repository = LinkRepository()

    def get(self, request, short_link):
        original_link = self.link_repository.get_original_link(short_link)
        return redirect(original_link)
