from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

from .views import BlogListView, BlogDetailView
urlpatterns += [
    path('blogs/', BlogListView.as_view(), name='blogs'),
    path('blogs/blog/<int:pk>/',BlogDetailView.as_view(), name='blog-detail')
]

