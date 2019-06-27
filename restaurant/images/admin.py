from django.contrib import admin

from images.models import MainBanner, BrandImage, BrandBanner, Menu, Franchise, FranchiseNotice

admin.site.register(MainBanner)
admin.site.register(BrandImage)
admin.site.register(BrandBanner)
admin.site.register(Menu)
admin.site.register(Franchise)
admin.site.register(FranchiseNotice)
