from django.urls import path, include
from home.views import index, about

urlpatterns = [
    path('', index),
    path('about/<int:filme_id>', about, name="about"),
]

