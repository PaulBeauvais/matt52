from django.contrib import admin
from .models import scavenges, complete_scavenges, finished_hunters

# Register your models here.


admin.site.register(scavenges)
admin.site.register(complete_scavenges)
admin.site.register(finished_hunters)

