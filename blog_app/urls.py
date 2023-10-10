from django.urls import path, include
from .views import home_page_view, HomePageView, AboutPageView

urlpatterns = [
    # path("", home_page_view, name="home_page_view"),
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about")
]