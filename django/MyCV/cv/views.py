from django.shortcuts import render
from .models import Profile
# Create your views here.

def front(req):
    data = Profile.objects.all()
    # took me too long to figure this out
    return render(req, "front.html", {"data": data})