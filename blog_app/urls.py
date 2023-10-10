from django.urls import path, include
from .views import home_page_view, HomePageView

urlpatterns = [
    # path("", home_page_view, name="home_page_view"),
    path("", HomePageView.as_view(), name="home")
]