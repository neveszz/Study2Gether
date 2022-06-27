from django.urls import path
from .views import home, room, create_room, update_room, deleteRoom


urlpatterns = [
    path('', home, name='home'),
    path('room/<int:pk>', room, name='room'),
    path('create_room/', create_room, name='create_room'),
    path('update_room/<str:pk>/', update_room, name='update_room'),
    path('delete_room/<str:pk>/', deleteRoom, name='delete_room')
]