from django.contrib import admin

from app_converter.models import UsersNoAuth, Files

# Register your models here.
admin.site.register(UsersNoAuth)
admin.site.register(Files)
