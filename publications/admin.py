from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import videos,cordination

#class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    #pass

admin.site.register(videos)
admin.site.register(cordination)
