from django.shortcuts import render, redirect
from .models import User, Project

# Create your views here.

user = None

def login(request):
    global user
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        if username != '' or password != '':
            users = User.objects.filter(username= username, password= password)
            print("consulta")
            if len(users) > 0:
                print(users[0])
                user = users[0]
                return redirect("index", users[0].username)
            else:
                print("usuario o contraseña erronea")
    return render(request, "login.html")

def logout(request):
    global user
    user = None
    return redirect("login")

def proyecto(request,id):
    if request.method == 'POST':
        photo = request.POST["photo"]
        title = request.POST["title"]
        description = request.POST["description"]
        github = request.POST["github"]
        checkbox = request.POST.getlist("checkbox")
        tags = []
        for check in checkbox:
            tags.append(check)

        if photo != '' or title != '' or description != '' or github != '':
            project = Project(photo=photo, title=title, description=description, tags=tags, url_github= github, user=user)
            project.save()
            return redirect("index", user.username)
    return render(request, "project.html")

def signup(request):
    if request.method == 'POST':
        username = request.POST["username"]
        name = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["passwordtwo"]
        if username != '' or name != '' or password != '' or password2 != '' or email != '':
            if password2 == password:
                user = User(username = username, password = password, name = name, email=email)
                user.save()
                return redirect("login")
    return render(request, "signup.html")

def index(request, username):
    global user
    user_context = {
        'id': user.id,
        'username': user.username,
        'name': user.name,
        'email': user.email
    }

    projects = Project.objects.filter(user= user)
    projects_dict = {
        "projects": projects
    }

    context = {
        'user': user,
        'projects': projects
    }
    print(projects_dict)
    print(projects)
    if user == None:
        return redirect("login")
    return render(request, "index.html", context= context)

def portfolio(request, id):
    pass