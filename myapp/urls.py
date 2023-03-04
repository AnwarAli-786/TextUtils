from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.index, name="index"),
    path('analyze', views.analyze, name="analyze"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    # path('spaceremove', views.spaceremove, name="spacerem"),
    # path('charcount', views.charcount, name="charcount"),
]

