from django.contrib import admin
from . models import events,documents,item_statistic

admin.site.register(events)
admin.site.register(documents)
admin.site.register(item_statistic)