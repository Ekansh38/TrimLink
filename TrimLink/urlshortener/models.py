from django.db import models


class Url(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=20000)
    short_url = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f'{self.url} - {self.short_url}'
