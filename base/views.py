from django.shortcuts import render, redirect
# from django.http import HttpResponse
    
from base.models import Room
from .forms import RoomForm

# Create your views here.

# rooms = [
#     {'id' : 0, 'name' : 'Lets learn python!'},
#     {'id' : 1, 'name' : 'Lets learn django!'},
#     {'id' : 2, 'name' : 'Lets learn scrapy!'},
#     {'id' : 3, 'name' : 'Lets learn aws!'},
# ]

def home(req):
    # return HttpResponse("Welcome To Home")
    
    rooms = Room.objects.all()
    print(type(rooms))
    print(rooms)
    context = {'rooms' : rooms}
    return render(req, 'base/home.html', context)

def room(req, id : str):
    # room = None
    
    # for r in rooms:
    #     if r["id"] == int(id):
    #         room = r
    
    room = Room.objects.get(id = id)
            
    context = {'room' : room}
    return render(req, 'base/room.html', context)


def create_room(request):
    form = RoomForm()
    
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    
    context = {'form' : form}

    return render(request, 'base/room_form.html', context)


def update_room(request, room_id):
    room = Room.objects.get(id = room_id)
    form = RoomForm(instance = room)
    print("first", form)
    
    if request.method == 'POST':
        form = RoomForm(request.POST, instance = room)
        print("first", form)
        
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form' : form}
    
    return render(request, 'base/room_form.html', context)

def delete_room(request, room_id):
    room = Room.objects.get(id = room_id)
    if request.method == 'POST':
       room.delete()
       
       return redirect("home")
   
    context = {'obj' : room}
    
    return render(request, 'base/delete.html', context)    


















