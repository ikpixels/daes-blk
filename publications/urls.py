from . import views
from django.urls import path

app_name = "publications"

urlpatterns = [
     
     path('videos/',views.Videos,name="videos"),
     path('videos2/<args>/',views.Videos,name="videos2"),
     path('videoform/',views.videoform,name="videoform"),
     path('aspForm/<int:id>/',views.aspForm,name="aspForm")
      
]
