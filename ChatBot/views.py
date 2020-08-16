from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
def ShowChatHome(request):
    return render(request,"ChatBot/chat_room.html")

def ShowChatPage(request,room_name,person_name):
    return render(request,"ChatBot/chat_screen.html",{'room_name':room_name,'person_name':person_name})
    #return HttpResponse("Chat page "+room_name+""+person_name)
