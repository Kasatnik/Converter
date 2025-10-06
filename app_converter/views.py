from django.core.files.storage import FileSystemStorage
from django.http import FileResponse
from django.shortcuts import render
import Files
from PIL import Image
import os


def jpg_to_png(input_path, output_path=None):
    try:
        # Открываем изображение
        with Image.open(input_path) as img:
            # Если выходной путь не указан, создаем его из входного
            if output_path is None:
                output_path = os.path.splitext(input_path)[0] + '.png'

            # Конвертируем и сохраняем как PNG
            img.save(output_path, 'PNG')
            print(f"Успешно сконвертировано: {input_path} -> {output_path}")

    except Exception as e:
        print(f"Ошибка при конвертации {input_path}: {e}")


def draw_home(request):
    if request.method == "POST":
        print(request.FILES)
        print(request.POST)
        fs = FileSystemStorage()
        print(request.FILES["file"].name)
        fs.save("inputimg/"+request.FILES["file"].name, request.FILES["file"])
        firstformat = request.FILES["file"].name.split(".")[-1]
        secondformat = request.POST["formatsphoto"]
        filename = "".join(request.FILES["file"].name.split(".")[:-1])
        print(firstformat)
        print(secondformat)
        jpg_to_png(f'inputimg/{filename}.{firstformat}', f'outputimg/{filename}.{secondformat}')
        return render(request, "home.html", {
            "link": f"download/{filename}.{secondformat}"})



    ip_address = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')

    print(f"IP адрес пользователя: {ip_address}")

    return render(request, "home.html", {
        'ip': ip_address})
def download(request, file_name):
    return FileResponse(open(f'outputimg/{file_name}', "rb"), as_attachment=True)

















