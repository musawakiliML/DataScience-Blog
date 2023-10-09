from django.shortcuts import render, HttpResponse

# Create your views here.

def home_page_view(request):
    return HttpResponse("Welcome to Data Science Blog")