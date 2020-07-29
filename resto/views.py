from django.shortcuts import render
from django.http import HttpResponse
from .models import SiteConfiguration


def index(request):
    context = {}
    site_configuration = SiteConfiguration.objects.get()
    context.update({
        "banners": [site_configuration.banner_image1, site_configuration.banner_image2, site_configuration.banner_image3],
        "site_details": {
            "site_name": site_configuration.site_name,
            "site_logo": site_configuration.site_logo,
            "site_info": site_configuration.site_info
        },
        "about_details": {
            "about": site_configuration.about,
            "about_description": site_configuration.about_description
        }
    })
    return render(request, "resto/home.html", context)
