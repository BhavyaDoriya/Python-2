from django.urls import path,include
from app2.views import home
urlpatterns = [
    path("app2/",home)
]