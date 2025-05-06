from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from treemenu.models import MenuItem

@admin.register(MenuItem)
class MenuItemAdmin(MPTTModelAdmin):
    mptt_level_indent = 20  # Отступ для иерархии
    list_display = ('name', 'parent', 'position', 'logged_in_only', 'guest_only') 
    list_editable = ('position',)  
    list_display_links = ('name',)  
    search_fields = ('name',)  
    list_filter = ('logged_in_only', 'guest_only')  