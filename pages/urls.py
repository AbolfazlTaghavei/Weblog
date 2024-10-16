from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_view, name='home'),
    path('aboutus/', views.aboutus_view, name='about_us'),
    path('contactus/', views.contactus_view, name='contact_us'),
]
