from django.shortcuts import render
from django.http import HttpResponse
from .models import SiteConfiguration


def index(request):
    context = {}
    site_configuration = SiteConfiguration.objects.get()
    context.update({
        "banners": [site_configuration.banner_image1, site_configuration.banner_image2, site_configuration.banner_image3]
    })
    return render(request, "resto/home.html", context)
