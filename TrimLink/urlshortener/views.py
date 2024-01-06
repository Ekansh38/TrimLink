from django.shortcuts import render


def index(request):
    return render(request, 'urlshortener/index.html')


def url(request, url_id):
    return render(request, 'urlshortener/url.html')
