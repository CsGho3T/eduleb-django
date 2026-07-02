from django.urls import path
from . import views
urlpatterns = [
    path("", views.blog, name="blog"),
    path("single/", views.blog_single, name="blog_single"),
]