from django.urls import path
from . import views

urlpatterns = [
    path('abcd/', views.post_list, name='post_list'),
]
