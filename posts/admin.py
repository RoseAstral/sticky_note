from django.contrib import admin
from .models import Post

class PostAdmin(admin.MolelAdmin):
  pass

admin.site.register(Post, PostAdmin)
