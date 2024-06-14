from django.shortcuts import render
from chat.models import Room 
# Create your views here.
def index(request):
    room_info = {
        'room_name': Room.objects.all(),
    }
    return render(request, 'index.html', room_info)