from . import views
from django.urls import path

app_name = "account"

urlpatterns = [
     
     path('Login/',views.Login,name="account"),
     path('Logout/',views.Logout,name="logout"),
     path('dashboard/',views.dashboard,name="dashboard"),
     path('PartinersForm/',views.Partiners,name="Partiners"),
     path('Team/',views.teamMember,name="TeamMember"),
     path('editTeam/<slug>/',views.EditTeam,name="EditTeam"),
     path('removemember/<int:id>/',views.removemember,name="removemember"),
     #path('register_view/',views.register_view,name="register_view")
   
    
]
