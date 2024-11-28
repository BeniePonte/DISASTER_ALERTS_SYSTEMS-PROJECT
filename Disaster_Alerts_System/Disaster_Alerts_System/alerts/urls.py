from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib.auth import views as auth_views
from . import views

# API router
router = DefaultRouter()
router.register(r'alerts', views.DisasterAlertViewSet, basename='disasteralert')

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
     path('logout/', auth_views.LogoutView.as_view(), name='logout'), 
    path('', views.list_alerts, name='list_alerts'),
    path('create/', views.create_alert, name='create_alert'),
    path('update/<int:alert_id>/', views.update_alert, name='update_alert'),
    path('api/', include(router.urls)),  # Include API routes
]