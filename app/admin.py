from django.contrib import admin
from django.contrib.auth.models import Group
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import Contact

# class ContactAdmin(admin.ModelAdmin):
class ContactAdmin(ImportExportModelAdmin):
    list_display = ('id','crime_title', 'crime_description', 'crime_location', 'lga', 'date_added')
    list_per_page = 5
    list_display_links = ('id', 'crime_title','crime_location')
    # list_editable = ('crime_title','lga')
    search_fields = ('crime_title', 'lga', 'street_address', 'date')
    # list_filter = ('crime_lga', 'crime_title', 'date_added')
    
admin.site.register(Contact, ContactAdmin)
# admin.site.unregister(Group)
