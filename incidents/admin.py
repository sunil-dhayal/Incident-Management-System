from django.contrib import admin
from .models import Incident

@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
    list_display = ('incident_id', 'description', 'priority', 'status', 'reporter', 'created_at')
    list_filter = ('priority', 'status', 'reporter')
    search_fields = ('incident_id', 'description')
    readonly_fields = ('incident_id','reporter','created_at')
