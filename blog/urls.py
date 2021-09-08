from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeListView.as_view(), name='blog-homepage'),
    path('about', views.AboutTemplateView.as_view(), name='blog-about'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='blog-post-detail'),
]