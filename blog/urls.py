from django.contrib.auth.decorators import login_required
from django.urls import  path
from . import views
from .views import PostListView, PostDetailView, UserListView, PostCreateView, PostUpdateView, PostDeleteView



urlpatterns = [
    path('', PostListView.as_view(), name="blog-home"),
    path('user/<str:username>/', UserListView.as_view(), name="user-posts"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('post/new/', login_required(PostCreateView.as_view(), login_url="login"), name="post-create"),
    path('post/<int:pk>/update/', login_required(PostUpdateView.as_view(), login_url="login"), name="post-update"),
    path('post/<int:pk>/delete/', login_required(PostDeleteView.as_view(), login_url="login"), name="post-delete"),
    path('about/', views.about, name='blog-about')
]