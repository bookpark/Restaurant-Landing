from django.shortcuts import render, get_object_or_404

from images.models import MainBanner


def index(request):
    return render(request, 'index.html')


def main_banners(request):
    banners = MainBanner.objects.all()
    context = {
        'banners': banners,
    }
    return render(request, 'index.html', context)


def main_banner(request, pk):
    banner = get_object_or_404(MainBanner, pk=pk)
    context = {
        'banner': banner,
    }
    return render(request, 'index.html', context)
