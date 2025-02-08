from django.urls import path
from .views import home  # Import your view

urlpatterns = [
    path('', home, name='home'),  # Define the URL pattern
]