from django.contrib import admin
from .models import Tree_Menu, Element_submenu

# Register your models here.


@admin.register(Element_submenu)
class MenuItemAdmin(admin.ModelAdmin):
    """
    Admin configuration for MenuItem model.
    """
    list_display = ('pk', 'title', 'parent')
    list_filter = ('menu',)
    search_fields = ('title', 'slug')
    ordering = ('pk',)


@admin.register(Tree_Menu)
class MenuAdmin(admin.ModelAdmin):
    """
    Admin configuration for Menu model.
    """
    list_display = ('title', 'slug')
    search_fields = ('title', 'slug')
