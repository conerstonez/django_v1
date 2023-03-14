from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello, name=' hello'),
    path('greet/', views.greet, name=' greet'),
    path('play/', views.play, name=' play'),
    path('learn/', views.learn, name="learn"),
    path('<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('', views.PostListView.as_view(), name='home'),
    path('new/', views.PostCreateView.as_view(), name='post_new'),
    ]
