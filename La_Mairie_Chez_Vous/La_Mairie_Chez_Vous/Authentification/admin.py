from django.contrib import admin

# Register your models here.
from .models import Agent, CustomUser


@admin.register(Agent)
class Agentadmin(admin.ModelAdmin):
    list_display = ['nom', 'mairie','num']

@admin.register(CustomUser)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'is_agent']    