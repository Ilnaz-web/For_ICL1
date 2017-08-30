from django.contrib import admin
from .models import *

class FilesAdmin(admin.ModelAdmin):
    list_display = ["name"]

    class Meta:
        model = Files

admin.site.register(Files, FilesAdmin)