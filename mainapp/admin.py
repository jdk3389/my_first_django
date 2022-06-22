# Register your models here.

from django.contrib import admin
from .models import Post, Ship, Review, Box

admin.site.register(Review)
admin.site.register(Post)
admin.site.register(Ship)
admin.site.register(Box)