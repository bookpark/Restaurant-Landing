from django.db import models


class Main(models.Model):
    image = models.ImageField(upload_to='main_banner')
