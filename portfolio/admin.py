from django.contrib import admin
from .models import Projet, PageProject


class ProjetPagesAdmin(admin.TabularInline):
    model = PageProject
    ordering = ('ordre',)
    extra = 0


@admin.register(Projet)
class ProjetsAdmin(admin.ModelAdmin):
    list_display = ('name', 'ordre')
    inlines = (ProjetPagesAdmin, )
    list_filter = ('name',)
    search_fields = ('name', 'description')
    ordering = ('ordre',)


# @admin.register(PageProject)
# class PagesAdmin(admin.ModelAdmin):
#     list_display = ('projet', 'numero')
