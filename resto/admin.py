from django.contrib import admin
from .models import SiteConfiguration, Menu, MenuType, Contact, Reservation

admin.site.register(SiteConfiguration)
admin.site.register(Menu)
admin.site.register(MenuType)
admin.site.register(Contact)
admin.site.register(Reservation)
