from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Room,Messages
# Create your views here.

@login_required
def rooms(request): #rooms list
    rooms = Room.objects.all()

    return render(request,'room/rooms.html',{'rooms':rooms})

@login_required
def room(request,slug): #inside room
    room = Room.objects.get(slug=slug)
    messages = Messages.objects.filter(room=room)[0:25]
    
    return render(request,'room/room.html',{'room':room, 'messages':messages})