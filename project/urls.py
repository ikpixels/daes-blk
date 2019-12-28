from . import views
from django.urls import path

app_name = "projects"

urlpatterns = [
     path('projects/',views.projects_view,name="projects"),
     path('projects2/<args>/',views.projects_view,name="projects2"),
     path('ProjectForm/',views.PjForm,name="PjForm"),
     path('PjDetail/<slug>/',views.PjDetail,name="PjDetail"),
     path('EditPj/<int:id>/',views.EditPj,name="EditPj"),
     path('removePj/<int:id>/',views.removePj,name="removePj"),
     path('pj_document_detail/<int:id>/',views.pj_document_detail,name="pj_document_detail")
]
