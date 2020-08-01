from django.db import models


class SiteConfiguration(models.Model):
    site_logo = models.CharField(max_length=200)
    site_name = models.CharField(max_length=50)
    site_info = models.TextField(max_length=300)
    banner_image1 = models.ImageField(upload_to="uploads/")
    banner_image2 = models.ImageField(upload_to="uploads/")
    banner_image3 = models.ImageField(upload_to="uploads/")
    # Contact Details
    about = models.CharField(max_length=200)
    about_description = models.TextField()
    phone_number = models.CharField(max_length=12)
    email = models.EmailField()
    city = models.CharField(max_length=50)
    address = models.TextField()
    # Google Map API Integration
    google_map_key = models.CharField(max_length=100)
    google_map_latitude = models.CharField(max_length=100)
    google_map_longitude = models.CharField(max_length=100)
    # Social Links
    facebook = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100)

    def __str__(self):
        return "Site Configuration"


class MenuType(models.Model):
    type = models.CharField(primary_key=True, max_length=50)

    def __str__(self):
        return self.type


class Menu(models.Model):
    menu_name = models.CharField(max_length=50)
    menu_type = models.ForeignKey(MenuType, on_delete=models.CASCADE)
    menu_price = models.FloatField()
    menu_description = models.TextField()
    menu_photo = models.ImageField(upload_to="uploads/")

    def __str__(self):
        return self.menu_name


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email_id = models.EmailField()
    mobile_no = models.CharField(max_length=12)
    message = models.CharField(max_length=200)


class Reservation(models.Model):
    reservation_date = models.DateField()
    reservation_from = models.DateTimeField()
    reservation_to = models.DateTimeField()
    total_persons = models.IntegerField()
    name = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=100)
    email_id = models.EmailField()

    def __str__(self):
        return self.id


class Gallery(models.Model):
    image_path = models.ImageField(upload_to="gallery/")
