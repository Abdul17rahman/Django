from django.shortcuts import render, redirect

# Create your views here.

tasks = [
    {"id": 1, "name": "Sleep"},
    {"id": 2, "name": "Eat"},
    {"id": 3, "name": "Walk"}
]

app_name = "tasks"

def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })

def add(request):
    if request.method == "POST":
        name = request.POST["name"]
        tasks.append({"id": 4, "name": name})
        return redirect("tasks:index")
    return render(request, "tasks/add.html")
