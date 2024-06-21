from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_resolution, name='add_resolution'),
    path('recommendations/', views.get_recommendations, name='get_recommendations'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='resolutions/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='resolutions/logout.html'), name='logout'),
    path('toggle_completed/<int:resolution_id>/', views.toggle_completed, name='toggle_completed'),
    path('profile/', views.profile, name='profile'),
    path('', views.resolution_list, name='resolution_list'),
    path('resolution/<int:pk>/', views.resolution_detail, name='resolution_detail'),
    path('resolution/<int:resolution_id>/add_progress/', views.add_progress, name='add_progress'),
    path('progress/', views.progress_view, name='progress'),
]
