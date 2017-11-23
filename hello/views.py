from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting


def db(request):
    greeting = Greeting()
    greeting.save()
    greetings = Greeting.objects.all()
    return render(request, 'hello/db.html', {'greetings': greetings})
