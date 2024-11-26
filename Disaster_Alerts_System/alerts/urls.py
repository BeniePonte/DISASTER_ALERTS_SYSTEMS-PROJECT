from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# API router
router = DefaultRouter()
router.register(r'alerts', views.DisasterAlertViewSet, basename='disasteralert')

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('logout/', views.user_logout, name='user_logout'), 
    path('', views.list_alerts, name='list_alerts'),
    path('create/', views.create_alert, name='create_alert'),
    path('update/<int:alert_id>/', views.update_alert, name='update_alert'),
    path('delete/<int:alert_id>/', views.delete_alert, name='delete_alert'),
    path('api/', include(router.urls)),  # Include API routes
]
