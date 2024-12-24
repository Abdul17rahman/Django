from django.shortcuts import render
from datetime import datetime

# Create your views here.

def newyaer(request):
    now = datetime.now()
    return render(request, "newyear/index.html", {
        "isNewYear": now.day == 1 and now.month == 1
    })

