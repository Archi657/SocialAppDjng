from django.contrib import admin
from .models import Post, Profile, Relationship


admin.site.register(Profile)
admin.site.register(Relationship)
admin.site.register(Post)
