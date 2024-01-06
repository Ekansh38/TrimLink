from django.shortcuts import render
from django.http import Http404
from django.shortcuts import redirect
import random

from .models import Url


nums = [i for i in range(9)]
chars = [chr(i) for i in range(65, 91)]
odds = ['k', 'e', ',', '4', 'a', 'b', 'a', '3', 'p', 'l']


def index(request):
    if request.method == 'POST':
        url = request.POST['url']
        short_url = create_shorturl()
        url = Url(url=url, short_url=short_url)
        url.save()
        return render(request, 'urlshortener/show.html', {'url': short_url})

    return render(request, 'urlshortener/index.html')


def url(request, url_id):
    short_urls = [url.short_url for url in Url.objects.all()]

    if url_id in short_urls:
        url = Url.objects.get(short_url=url_id)
        url = url.url
        try:
            return redirect(url)
        except:
            return Http404()

    return Http404()


def url_exists(short_url):
    short_urls = [url.short_url for url in Url.objects.all()]
    if short_url in short_urls:
        return True

    return False


def build_shorturl():
    short_url = ''

    short_url += random.choice(chars)
    short_url += str(random.choice(nums))
    short_url += random.choice(odds)
    short_url += random.choice(chars)
    short_url += str(random.choice(nums))
    short_url += random.choice(odds)

    return short_url


def create_shorturl():
    short_url = build_shorturl()

    while url_exists(short_url):
        short_url = build_shorturl()

    return short_url
