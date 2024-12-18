from django.contrib import admin
from .models import Post, Contact, Comment


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ['title']}

class CommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Contact)
admin.site.register(Comment, CommentAdmin)