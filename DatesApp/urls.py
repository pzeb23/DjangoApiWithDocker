from django.urls import re_path
from DatesApp import views

urlpatterns=[
    re_path(r'^dates$',views.datesApi),
    re_path(r'^dates/([0-9]+)$',views.datesApi),
    re_path(r'^popular$',views.popularApi)
]