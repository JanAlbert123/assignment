from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('announcements/', views.announcement_list, name='announcement_list'),
    path('announcements/<int:id>/', views.announcement_detail, name='announcement_detail'),
    path("announcement1/", views.announcement1, name="announcement1"),
    path("announcement2/", views.announcement2, name="announcement2"),
]