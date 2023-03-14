from django.urls import path
from post import views

urlpatterns = {
    path('hello/', views.hello, name='hello'),
    path('greet/', views.greet, name='greet'),
    path('bye/', views.bye, name='bye'),
}
