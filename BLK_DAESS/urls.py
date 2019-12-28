from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django .conf.urls. static import static
from django .conf import settings
#from myco import views
from django.views.static import serve
from django.conf.urls import handler404, handler500


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("index.urls")),
    path('account/',include("account.urls")),
    path('event/',include('event.urls')),
    path('products/',include('products.urls')),
    path('donation/',include('donation.urls')),
    path('publications/',include('publications.urls')),
    path('achievement/',include('achievement.urls')),
    path('career/',include("career.urls")),
    path('project/',include("project.urls")),
    path('paypal/', include('paypal.standard.ipn.urls')),
   
]

#handler404 = views.error_404
#handler500 = views.error_500


urlpatterns+=staticfiles_urlpatterns()

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
