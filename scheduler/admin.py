from .models import CommunicationScheduling
from django.contrib import admin


@admin.register(CommunicationScheduling)
class CommunicationSchedulingAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'message', 'message_type', 'recipient',
        'scheduling', 'status', 'created_at'
    )
    search_fields = ('message', 'recipient')
    list_filter = ('message_type', 'status',)
