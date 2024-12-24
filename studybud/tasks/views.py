from django.shortcuts import render, redirect

# Create your views here.

app_name = "tasks"

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []

    print(request.session["tasks"])
    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })

def add(request):
    if request.method == "POST":
        name = request.POST["name"]
        task = {"id": len(request.session["tasks"]) + 1, "name": name}
        request.session["tasks"].append(task)
        request.session.modified = True
        return redirect("tasks:index")
    return render(request, "tasks/add.html")
