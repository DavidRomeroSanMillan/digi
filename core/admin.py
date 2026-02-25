from django.contrib import admin
from .models import Item, Client, Room


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'created')


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'created')


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('number', 'beds', 'created')
    filter_horizontal = ('occupants',)
