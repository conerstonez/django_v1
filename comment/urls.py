from django.urls import path
from comment import views

urlpatterns = {
    path('v1/', views.first_comment, name='comment'),
    path('greet/', views.greet, name='greet'),
}
