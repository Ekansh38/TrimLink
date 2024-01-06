from django.urls import path

from . import views


urlpatterns = [
        path('', views.index, name='index'),
        path('<str:url_id>', views.url, name='url')
    ]
