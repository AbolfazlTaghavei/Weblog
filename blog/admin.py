from django.contrib import admin
from . import models

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author' ,'datetime_modified', 'title', 'status', )
    ordering = ('-status', '-datetime_modified', )
