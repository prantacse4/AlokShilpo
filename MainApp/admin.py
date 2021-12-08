from django.contrib import admin
from .models import *
# Register your models here.


class MessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'email', 'mymessage']

admin.site.register(Message, MessageAdmin)