from . import views
from django.urls import path

app_name = "event"

urlpatterns = [
     path('event/',views.event,name="event"),
     path('eventasp/<asp>/',views.event,name="event2"),
     path('event_detail/<slug>/',views.event_detail,name="event_detail"),
     path('event_form/',views.event_form,name="event_form"),
     path('document_view/',views.document_view,name="document_view"),
     path('DocuForm/',views.DocuForm,name="DocuForm"),
     path('Editevent/<int:id>/',views.Editevent,name="Editevent"),
     path('RemoveEvent/<int:id>/',views.RemoveEvent,name="RemoveEvent"),
     path('document_detail/<int:id>/',views.document_detail,name="document_detail")  
]
