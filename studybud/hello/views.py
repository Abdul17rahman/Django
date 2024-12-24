from django.shortcuts import render

# Create your views here.

def hello(request):
    return render(request, "hello/index.html")

def greet(request, name=None):
    return render(request, "hello/greet.html", {
        "name": name.capitalize() if name else "Anonymous"
    })
