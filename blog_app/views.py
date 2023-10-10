from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView, ListView
from .models import Post

# Create your views here.

def home_page_view(request):
    return HttpResponse("Welcome to Data Science Blog")

class AboutPageView(TemplateView):
    template_name = 'about.html'

class BlogListView(ListView):
    model = Post
    template_name = 'index.html'