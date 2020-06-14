from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    # path('', views.home, name='blog-home'), # url for function base view
    path('', views.PostListView.as_view(), name='blog-home'),  # url for class based view
    path('user/<str:username>/', views.UserPostListView.as_view(), name='user-posts'),
    path('about/', TemplateView.as_view(template_name='blog/about.html', ), name='blog-about'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', views.PostDeleteView.as_view(), name='post-delete'),
]
