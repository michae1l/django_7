from django.urls import path
from .views import index,home

urlpatterns = [
    path('', index, name="hotel_recorde"),
    path('home/', home, name="home")
]