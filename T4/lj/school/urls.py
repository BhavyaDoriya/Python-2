from django.urls import path
from school.views import home,table,info,form,update,delete
urlpatterns=[
    path("home/",home,name="home"),
    path("table/",table,name="table"),
    path("info/<int:facid>/",info,name="info"),
    path("form/",form,name="form"),
    path("update/<int:id>/",update,name="update"),
    path("delete/<int:id>/",delete,name="delete")
]