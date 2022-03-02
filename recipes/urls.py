from django.urls import path

from recipes.views import about, contact, home

urlpatterns = [
    path('', home),  # Home
    path('about/', about),  # /About/
    path('contact/', contact),  # /Contact/
]
