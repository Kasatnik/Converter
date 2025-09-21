from django.db import models


class UsersNoAuth(models.Model):
    number_files = models.IntegerField()
    ip = models.TextField(max_length=65534)

    class Meta:
        db_table = 'users_no_auth'
        # Если поле 'id' должно быть автоинкрементным, Django создаст его автоматически

    def __str__(self):
        return f"{self.ip} , {self.number_files}"


class Files(models.Model):
    filename = models.TextField(max_length=65535)
    user = models.ForeignKey(UsersNoAuth, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.filename} | {self.user}"

    class Meta:
        db_table = 'filed'
        # Поле 'id' будет создано автоматически как автоинкрементное
