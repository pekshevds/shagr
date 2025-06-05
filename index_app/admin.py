from django.contrib import admin
from django.conf import settings

admin.site.site_header = f"Панель администрирования {settings.CURRENT_HOST}"
admin.site.site_title = f"Панель администрирования {settings.CURRENT_HOST}"
admin.site.index_title = "Добро пожаловать!"
