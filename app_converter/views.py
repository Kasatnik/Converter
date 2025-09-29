from django.core.files.storage import FileSystemStorage
from django.shortcuts import render

def draw_home(request):
    if request.method == "POST":
        print(request.FILES)
        print(request.POST)
        fs = FileSystemStorage()
        print(request.FILES["file"].name)
        fs.save(request.FILES["file"].name, request.FILES["file"])

    ip_address = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')

    print(f"IP адрес пользователя: {ip_address}")

    return render(request, "home.html", {
        'ip': ip_address})

