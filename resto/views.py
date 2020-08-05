from django.shortcuts import render
from django.http import HttpResponse
from .models import SiteConfiguration, MenuType, Menu, Gallery, CustomerReview


def index(request):
    context = {}
    site_configuration = SiteConfiguration.objects.get()
    context.update({
        "gallery": Gallery.objects.all(),
        "customer_review": CustomerReview.objects.all()
    })
    context.update(get_common())
    context.update(get_menu_details())
    return render(request, "resto/home.html", context)


def menus(request):
    context = {}
    context.update(get_common())
    context.update(get_menu_details())
    return render(request, "resto/menus.html", context)


def get_common():
    site_configuration = SiteConfiguration.objects.get()
    return {
        "phone": site_configuration.phone_number,
        "email": site_configuration.email,
        "city": site_configuration.city,
        "address": site_configuration.address,
        "social": {
            "facebook": site_configuration.facebook,
            "twitter": site_configuration.twitter,
            "instagram": site_configuration.instagram,
            "linkdin": site_configuration.linkedin
        },
        "site_details": {
            "site_name": site_configuration.site_name,
            "site_logo": site_configuration.site_logo,
            "site_info": site_configuration.site_info
        },
        "about_details": {
            "about": site_configuration.about,
            "about_description": site_configuration.about_description
        },
        "banners": [site_configuration.banner_image1, site_configuration.banner_image2,
                    site_configuration.banner_image3],
    }


def get_menu_details():
    return {
        "menu_type": MenuType.objects.all(),
        "menus": Menu.objects.all(),
    }
