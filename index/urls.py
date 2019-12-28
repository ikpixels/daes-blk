from . import views
from django.urls import path

app_name = "index"

urlpatterns = [
     
     path('',views.index,name="index"),
     path('about_daess/',views.about_daess,name="about_daess"),
     path('contact/',views.contact,name="contact"),
     path('DaessoBjectives/',views.daess_objectives,name="objective"),
     path('DaessStructure/',views.daess_structure,name="structure"),
     path('team/',views.team,name="team"),
     path('team2/<args>/',views.team,name="team2"),
     path('ASP/<asp>/',views.ASP,name="ASP"),
     path('Subscribe/',views.Subscribe,name="Subscribe"),
     path('unsubscribe/',views.unsubscribe,name="unsubscribe"),
     path('team_detail/<slug>/',views.tema_detail,name="tema_detail")
]
