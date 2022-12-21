from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


class HomePageView(TemplateView):  # capital HomePageView since it is class
    template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = "about.html"


# def homePageView(request):     # lowercase homePageView since it is a function
# return HttpResponse("Hello, World!")


# Create your views here.
