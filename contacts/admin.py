from django.contrib import admin
from .models import Category, Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id',  'name', 'last_name',
                    'telephone', 'email', 'category', 'show')
    list_display_links = ('id',  'name', 'last_name')
    list_filter = ('category',)
    list_per_page = 10
    search_fields = ('id', 'name', 'last_name', 'telephone', 'email')
    list_editable = ('telephone', 'show')


admin.site.register(Category)
admin.site.register(Contact, ContactAdmin)
