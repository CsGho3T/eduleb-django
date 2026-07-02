from django.urls import path
from . import views
urlpatterns = [
    path("", views.instructer, name="instructor"),
    path("ins_details/", views.ins_details, name="ins_details"),
]