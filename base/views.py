from django.shortcuts import render
# from django.http import HttpResponse

from base.models import Room

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
    context = {}
    return render(request, 'base/room_form.html', context)