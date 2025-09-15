from django.db import models

class UseraNoAuto(models.Model):
    number_files = models.IntegerField()
    ip = models.TextField(max_length=65535)

    class Meta:
        db_table = 'usera_no_auto'
        # Если поле 'id' должно быть автоинкрементным, Django создаст его автоматически


class Filed(models.Model):
    filename = models.TextField(max_length=65535)

    class Meta:
        db_table = 'filed'
        # Поле 'id' будет создано автоматически как автоинкрементное

# Если есть связь между таблицами, добавьте ForeignKey
# Например, если filed связана с usera_no_auto:
# class Filed(models.Model):
#     user = models.ForeignKey(UseraNoAuto, on_delete=models.CASCADE)
#     filename = models.TextField(max_length=65535)