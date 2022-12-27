from django.urls import path

# from .views import homePageView
from .views import HomePageView, AboutPageView

# we use .as_view() when useing a Class-Based View in 'views.py'
urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"),
    path("", HomePageView.as_view(), name="home"),
    # path("", homePageView, name="home"),
]
