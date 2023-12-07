from django.shortcuts import render, redirect
# from django.http import HttpResponse
    
from base.models import Room, Topic
from .forms import RoomForm
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

# rooms = [
#     {'id' : 0, 'name' : 'Lets learn python!'},
#     {'id' : 1, 'name' : 'Lets learn django!'},
#     {'id' : 2, 'name' : 'Lets learn scrapy!'},
#     {'id' : 3, 'name' : 'Lets learn aws!'},
# ]

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        print(username, password)
        
        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, "User does not exist")
            return redirect("login")
        
        user = authenticate(request, username = username, password = password)
        
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid Credentials")
            return redirect("login")
    
    context = {}
    
    return render(request, 'base/login_register.html', context)

def user_logout(request):
    logout(request)
    return redirect("home")

def home(request):
    # return HttpResponse("Welcome To Home")
    
    topic = request.GET.get("topic") if request.GET.get('topic') != None else ''
    
    rooms = Room.objects.filter(
        Q(topic__name__icontains = topic) |
        Q(name__icontains = topic) |
        Q(description__icontains = topic)
    )
    
    topics = Topic.objects.all()
    context = {'rooms' : rooms, 'topics' : topics, 'room_count' : len(rooms)}
    
    return render(request, 'base/home.html', context)

def room(request, id : str):
    # room = None
    
    # for r in rooms:
    #     if r["id"] == int(id):
    #         room = r
    
    room = Room.objects.get(id = id)
            
    context = {'room' : room}
    return render(request, 'base/room.html', context)


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