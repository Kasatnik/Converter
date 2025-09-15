from django.shortcuts import render

def draw_home(request):
    return render(request, "home.html")