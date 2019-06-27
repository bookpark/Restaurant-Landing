from django.db import models


class MainBanner(models.Model):
    main = models.ImageField(upload_to='main_banner')

    def __str__(self):
        return f'메인 배너 - [{self.main.name}]'


class BrandImage(models.Model):
    brand = models.ImageField(upload_to='main_brand')

    def __str__(self):
        return f'브랜드 페이지 - [{self.brand.name}]'


class BrandBanner(models.Model):
    brand_banner_1 = models.ImageField(upload_to='brand_banner_1')
    brand_banner_2 = models.ImageField(upload_to='brand_banner_2')

    def __str__(self):
        return f'브랜드 배너 (이미지 두장) - [{self.brand_banner_1.name}, {self.brand_banner_2.name}]'


class Menu(models.Model):
    menu = models.ImageField(upload_to='menu')

    def __str__(self):
        return f'메뉴 - [{self.menu.name}]'


class Franchise(models.Model):
    franchise_1 = models.ImageField(upload_to='franchise_1')
    franchise_2 = models.ImageField(upload_to='franchise_2')
    franchise_3 = models.ImageField(upload_to='franchise_3')
    franchise_4 = models.ImageField(upload_to='franchise_4')

    def __str__(self):
        return f'가맹점 소개 - 이미지 네장'


class FranchiseNotice(models.Model):
    franchise_notice = models.ImageField(upload_to='franchise_notice')

    def __str__(self):
        return f'가맹 안내'
