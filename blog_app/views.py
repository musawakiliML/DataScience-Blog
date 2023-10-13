from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from .models import Post

# Create your views here.

def home_page_view(request):
    return HttpResponse("Welcome to Data Science Blog")

class AboutPageView(TemplateView):
    template_name = 'about.html'

class BlogListView(ListView):
    model = Post
    template_name = 'index.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = "__all__"

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ["title", "slug", "body", "status"]