from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView

# Create your views here.

def home_page_view(request):
    return HttpResponse("Welcome to Data Science Blog")

class HomePageView(TemplateView):
    template_name = 'index.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'