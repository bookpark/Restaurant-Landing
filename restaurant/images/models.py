from django.db import models


class MainBanner(models.Model):
    image = models.ImageField(upload_to='main_banner')
