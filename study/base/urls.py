from django.urls import path
from .views import home, room, create_room, update_room, deleteRoom, login_page, logout_user, register_user, \
    deleteMessage, user_profile, updateUser, topicsPage

urlpatterns = [
    path('login/', login_page, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name='register'),
    path('', home, name='home'),
    path('room/<int:pk>', room, name='room'),
    path('profile/<str:pk>', user_profile, name='user_profile'),
    path('create_room/', create_room, name='create_room'),
    path('update_room/<str:pk>/', update_room, name='update_room'),
    path('delete_room/<str:pk>/', deleteRoom, name='delete_room'),
    path('delete_message/<str:pk>/', deleteMessage, name='delete_message'),
    path('update_user/', updateUser, name='update_user'),
    path('topics/', topicsPage, name='topics')
]