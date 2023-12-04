from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

rooms = [
    {'id' : 0, 'name' : 'Lets learn python!'},
    {'id' : 1, 'name' : 'Lets learn django!'},
    {'id' : 2, 'name' : 'Lets learn scrapy!'},
    {'id' : 3, 'name' : 'Lets learn aws!'},
]

def home(req):
    # return HttpResponse("Welcome To Home")
    context = {'rooms' : rooms}
    return render(req, 'base/home.html', context)

def room(req, id : str):
    room = None
    
    for r in rooms:
        if r["id"] == int(id):
            room = r
            
    context = {'room' : room}
    return render(req, 'base/room.html', context)