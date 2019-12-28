from . import views
from django.urls import path

app_name = "career"

urlpatterns = [
     
     path('job/',views.Job_list,name="job"),
     path('job_detail/<slug>/',views.job_detail,name="job_detail"),
     path('job_category/<cat>/',views.Job_list,name="job_category"),
     path('job_form/',views.job_form,name="job_form"),
     path('EditJob/<int:id>/',views.EditJob,name="EditJob"),
     path('remove_job/<int:id>/',views.remove_job,name="remove_job")  
]
