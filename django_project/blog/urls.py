from django.urls import path
from . import views
from .views import (
    PostUpdateView,
    PostView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostView
    )
urlpatterns = [
    path('', PostView.as_view(),name="blog-home"),
    path('about/', views.about,name="blog-about"),
    path('post/<int:pk>/', PostDetailView.as_view(),name="post-detail"),
    path('post/<int:pk>/update', PostUpdateView.as_view(),name="post-update"),
    path('post/<int:pk>/delete', PostDeleteView.as_view(),name="post-delete"),
    path('post/new/', PostCreateView.as_view(),name="post-create"),
    path('user/<str:username>/', UserPostView.as_view(),name="user-posts"),
]
