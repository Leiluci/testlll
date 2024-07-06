from django.contrib import admin
from .models import InstagramUser

@admin.register(InstagramUser)
class InstagramUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username')
    search_fields = ('username',)
