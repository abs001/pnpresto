from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    path('', views.index, name='index'),
    # url(r'^resto/menus/$', views.menus, name='menus')
    path('menus/', views.menus, name='menus'),
]