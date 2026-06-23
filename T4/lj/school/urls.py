from django.urls import path
from school.views import home,table,info,form
urlpatterns=[
    path("home/",home,name="home"),
    path("table/",table,name="table"),
    path("info/<int:facid>/",info,name="info"),
    path("form/",form,name="form")
]