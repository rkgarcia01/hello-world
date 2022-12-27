from django.urls import path

# from .views import homePageView
from .views import HomePageView, AboutPageView

urlpatterns = [
    path(
        "about/", AboutPageView.as_view(), name="about"
    ),  # we use .as_view() when useing a Class-Based View in 'views.py'
    path(
        "", HomePageView.as_view(), name="home"
    ),  # we use .as_view() when useing a Class-Based View in 'views.py'
    # path("", homePageView, name="home"),
]
