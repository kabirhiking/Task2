from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    available_seats = models.PositiveIntegerField()
    
    def __str__(self):
        return self.title

class Registration(models.Model):
    event = models.ForeignKey(Event, related_name='registrations', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='registrations', on_delete=models.CASCADE)
    registered_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.event.title}"
