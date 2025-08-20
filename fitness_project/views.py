from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def bootstrap_example(request):
    return render(request, "bootstrap_example.html")
