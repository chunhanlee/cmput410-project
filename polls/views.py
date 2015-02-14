from django.shortcuts import render

from polls.models import Authors, Friends, Posts, Comments, GithubStreams, TwitterStreams, FacebookStreams

from django.http import HttpResponse
from .models import Greeting
# Create your views here.
def index(request):
    return HttpResponse ("Hey, you're in polls.")

def mainpage(request):
    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, './templates/mainpage.html', {'greetings': greetings})
