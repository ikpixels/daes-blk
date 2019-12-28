from . import views
from django.urls import path

app_name = "give"

urlpatterns = [
     path('donation/',views.donation,name="donation"),
     path('mpamba/',views.mpamba,name="mpamba"),
     path('mpamba2/',views.mpamba2,name="mpamba2"),
     path('airtelmoney/',views.airtelmoney,name="airtelmoney"),
     path('airtelmoney2/',views.airtelmoney2,name="airtelmoney2"),
     path('donation_thax/',views.donation_thax,name="donation_thax"),
     path('donation_thax2/',views.donation_thax2,name="donation_thax2"),
     path('donation_view/',views.donation_view,name="donation_view")
]
