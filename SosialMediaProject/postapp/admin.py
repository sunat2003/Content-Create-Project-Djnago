from django.contrib import admin
from postapp.models import PostModel


class PostModelAdmin(admin.ModelAdmin):
    list_display=['user','text','photo']
admin.site.register(PostModel,PostModelAdmin)


