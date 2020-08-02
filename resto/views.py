from django.shortcuts import render
from django.http import HttpResponse
from .models import SiteConfiguration, MenuType, Menu, Gallery, CustomerReview


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
        },
        "menu_type": MenuType.objects.all(),
        "menus": Menu.objects.all(),
        "gallery": Gallery.objects.all(),
        "customer_review": CustomerReview.objects.all(),
        "phone": site_configuration.phone_number,
        "email": site_configuration.email,
        "city": site_configuration.city,
        "address": site_configuration.address,
        "social": {
            "facebook": site_configuration.facebook,
            "twitter": site_configuration.twitter,
            "instagram": site_configuration.instagram,
            "linkdin": site_configuration.linkedin
        }
    })
    return render(request, "resto/home.html", context)
