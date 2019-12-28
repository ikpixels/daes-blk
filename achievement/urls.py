from . import views
from django.urls import path

app_name = "achievement"

urlpatterns = [
     
     path('Achievement/',views.Achievement,name="achievement"),
     path('Achievement_detail/<slug>/',views.Achievement_detail,name="detail"),
     path('Achievement_form/',views.Achievement_form,name="Achievement_form"),
     path('EditAchievement/<int:id>/',views.EditAchievement,name="EditAchievement"),
     path('remove_stroy/<int:id>/',views.remove_stroy,name="remove_stroy")
      
]
