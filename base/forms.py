from django.forms import ModelForm
from .models import Room, User

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields =   '__all__'
        # fields = ['name', 'description', 'title'] 
        exclude = ['host', 'participants']

class UserForm(ModelForm):
    class Meta:
        model = User 
        fields = ['username', 'email']
        