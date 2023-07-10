from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    return render(request, "core/home.html")


def about(request):
    return render(request, "core/about.html")


def contact(request):
    return render(request, "core/contact.html")


def projects(request):

    return render(request, "core/projects.html")


def tasks(request):
    return render(request, "core/tasks.html")
