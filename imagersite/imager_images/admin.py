from django.contrib import admin

from .models import Album, Photo

# Register your models here.
admin.site.register(Photo)
admin.site.register(Album)
