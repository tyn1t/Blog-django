from django.urls import path 
from .views import PostAPIView, ListAPIView

urlpatterns = [
    path("blog/", ListAPIView.as_view(), name="blog"),
    path("posts/blog_form/", PostAPIView.as_view(),  name="blog_form")
]