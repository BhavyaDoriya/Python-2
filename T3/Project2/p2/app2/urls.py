from django.urls import path,include
from app2.views import home
from app2.views import about,nav
urlpatterns = [
    path("home/",home,name='home'),
    path("about/",about,name='about'),
    path("nav/",nav,name='nav')
]