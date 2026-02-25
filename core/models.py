from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Room(models.Model):
    number = models.CharField(max_length=10, unique=True)
    beds = models.PositiveSmallIntegerField(default=1)
    description = models.TextField(blank=True)
    occupants = models.ManyToManyField(Client, blank=True, related_name='rooms')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Habitación {self.number}"
