from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeListView.as_view(), name='blog-homepage'),
    path('about', views.about, name='blog-about'),
]