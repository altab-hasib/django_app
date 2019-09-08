from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'gender', 'email', 'info', 'phone')
    list_display_links = ('id', 'name')
    list_editable = ('info',)
    list_per_page = 5
    search_fields = ('name', 'gender', 'email', 'info', 'phone')
    list_filter = ('gender', 'date_added')


admin.site.register(Contact, ContactAdmin)

