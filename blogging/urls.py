from django.urls import path
from blogging.views import BlogDetailView
from blogging.views import BlogListView

urlpatterns = [
    path('', BlogListView.as_view(), name="blog_index"),
    path('posts/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
]