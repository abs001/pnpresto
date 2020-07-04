from django.db import models


class SiteConfiguration(models.Model):
    site_logo = models.CharField()
    site_name = models.CharField()
    site_info = models.TextField()
    banner_image1 = models.ImageField()
    banner_image2 = models.ImageField()
    banner_image3 = models.ImageField()
    # Contact Details
    about = models.CharField()
    about_description = models.TextField()
    phone_number = models.CharField()
    email = models.EmailField()()
    city = models.CharField()
    address = models.TextField()
    # Google Map API Integration
    google_map_key = models.CharField()
    google_map_latitude = models.CharField()
    google_map_longitude = models.CharField()
    # Social Links
    facebook = models.CharField()
    twitter = models.CharField()
    instagram = models.CharField()
    linkedin = models.CharField()


class MenuType(models.Model):
    type = models.CharField(primary_key=True)


class Menu(models.Model):
    menu_name = models.CharField()
    menu_type = models.ForeignKey(MenuType, on_delete=models.CASCADE())
    menu_price = models.FloatField()
    menu_description = models.TextField()
    menu_photo = models.ImageField()


class Contact(models.Model):
    name = models.CharField()
    email_id = models.EmailField()
    mobile_no = models.CharField()
    message = models.CharField()


class Reservation(models.Model):
    reservation_date = models.DateField()
    reservation_from = models.DateTimeField()
    reservation_to = models.DateTimeField()
    total_persons = models.IntegerField()
    name = models.CharField()
    mobile_no = models.CharField()
    email_id = models.EmailField()