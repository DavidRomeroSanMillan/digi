from django.urls import path
from . import views

urlpatterns = [
    path('', views.ItemListView.as_view(), name='item-list'),
    path('item/<int:pk>/', views.ItemDetailView.as_view(), name='item-detail'),
    path('item/add/', views.ItemCreateView.as_view(), name='item-add'),
    path('item/<int:pk>/edit/', views.ItemUpdateView.as_view(), name='item-edit'),
    path('item/<int:pk>/delete/', views.ItemDeleteView.as_view(), name='item-delete'),
    # Clients
    path('clients/', views.ClientListView.as_view(), name='client-list'),
    path('clients/add/', views.ClientCreateView.as_view(), name='client-add'),
    path('clients/<int:pk>/', views.ClientDetailView.as_view(), name='client-detail'),
    path('clients/<int:pk>/edit/', views.ClientUpdateView.as_view(), name='client-edit'),
    path('clients/<int:pk>/delete/', views.ClientDeleteView.as_view(), name='client-delete'),
    # Rooms
    path('rooms/', views.RoomListView.as_view(), name='room-list'),
    path('rooms/add/', views.RoomCreateView.as_view(), name='room-add'),
    path('rooms/<int:pk>/', views.RoomDetailView.as_view(), name='room-detail'),
    path('rooms/<int:pk>/edit/', views.RoomUpdateView.as_view(), name='room-edit'),
    path('rooms/<int:pk>/delete/', views.RoomDeleteView.as_view(), name='room-delete'),
    path('rooms/<int:pk>/assign/', views.assign_client, name='room-assign-client'),
    path('rooms/<int:room_pk>/remove/<int:client_pk>/', views.remove_client, name='room-remove-client'),
]
