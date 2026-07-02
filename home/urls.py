from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="home"),
    path("index2/", views.index2, name="index2"),
    path("about/", views.about, name="about"),
    path("faq/", views.faq, name="faq"),
    path("404/", views.error_404, name="error_404"),
    path("pricing/", views.pricing, name="pricing"),
]