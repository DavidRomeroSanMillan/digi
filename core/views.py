from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, Client, Room


class ItemListView(ListView):
    model = Item
    template_name = 'core/item_list.html'


class ItemDetailView(DetailView):
    model = Item
    template_name = 'core/item_detail.html'


class ItemCreateView(CreateView):
    model = Item
    fields = ['name', 'description']
    template_name = 'core/item_form.html'
    success_url = reverse_lazy('item-list')


class ItemUpdateView(UpdateView):
    model = Item
    fields = ['name', 'description']
    template_name = 'core/item_form.html'
    success_url = reverse_lazy('item-list')


class ItemDeleteView(DeleteView):
    model = Item
    template_name = 'core/item_confirm_delete.html'
    success_url = reverse_lazy('item-list')


# --- Client Views ---
class ClientListView(ListView):
    model = Client
    template_name = 'core/client_list.html'


class ClientDetailView(DetailView):
    model = Client
    template_name = 'core/client_detail.html'


class ClientCreateView(CreateView):
    model = Client
    fields = ['first_name', 'last_name', 'email', 'phone']
    template_name = 'core/client_form.html'
    success_url = reverse_lazy('client-list')


class ClientUpdateView(UpdateView):
    model = Client
    fields = ['first_name', 'last_name', 'email', 'phone']
    template_name = 'core/client_form.html'
    success_url = reverse_lazy('client-list')


class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'core/client_confirm_delete.html'
    success_url = reverse_lazy('client-list')


# --- Room Views ---
class RoomListView(ListView):
    model = Room
    template_name = 'core/room_list.html'


class RoomDetailView(DetailView):
    model = Room
    template_name = 'core/room_detail.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['clients'] = Client.objects.all()
        return ctx


class RoomCreateView(CreateView):
    model = Room
    fields = ['number', 'beds', 'description']
    template_name = 'core/room_form.html'
    success_url = reverse_lazy('room-list')


class RoomUpdateView(UpdateView):
    model = Room
    fields = ['number', 'beds', 'description']
    template_name = 'core/room_form.html'
    success_url = reverse_lazy('room-list')


class RoomDeleteView(DeleteView):
    model = Room
    template_name = 'core/room_confirm_delete.html'
    success_url = reverse_lazy('room-list')


def assign_client(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == 'POST':
        client_id = request.POST.get('client')
        if client_id:
            client = get_object_or_404(Client, pk=client_id)
            room.occupants.add(client)
    return redirect('room-detail', pk=pk)


def remove_client(request, room_pk, client_pk):
    room = get_object_or_404(Room, pk=room_pk)
    client = get_object_or_404(Client, pk=client_pk)
    room.occupants.remove(client)
    return redirect('room-detail', pk=room_pk)
