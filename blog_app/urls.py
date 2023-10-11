from django.urls import path, include
from .views import home_page_view, BlogListView, AboutPageView, BlogDetailView

urlpatterns = [
    # path("", home_page_view, name="home_page_view"),
    path("", BlogListView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail")
]