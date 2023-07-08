from django.urls import path

from .views import HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("articles/", HomePageView.as_view(), name="home1"),

]
