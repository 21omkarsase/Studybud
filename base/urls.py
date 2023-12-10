from django.urls import path 
from . import views


urlpatterns = [
    path('', views.home, name = "home"),
    path('room/<str:room_id>/', views.room, name = "room"),
    path('create-room/', views.create_room, name = "create-room"),
    path("update-room/<str:room_id>/", views.update_room, name = 'update-room'),
    path("delete-room/<str:room_id>/", views.delete_room, name = 'delete-room'),
    path("login/", views.user_login, name = "login"),
    path("register/", views.user_register, name = 'register'),
    path("logout/", views.user_logout, name = "logout"),
    path('delete-message/<str:message_id>', views.delete_message, name = 'delete-message'),
    path('user-profile/<str:user_id>', views.user_profile, name = 'user-profile'),
    path('update-user', views.update_user, name = "update-user"),
]