from django.contrib import admin

# Register your models here.
from .models import Skills, Post, Tag

admin.site.register(Skills)
admin.site.register(Post)
admin.site.register(Tag)