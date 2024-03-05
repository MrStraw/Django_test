from django.contrib import admin
from .models import Projet, PageProject


class ProjetPagesAdmin(admin.TabularInline):
    model = PageProject
    ordering = ('ordre',)
    extra = 0


@admin.register(Projet)
class ProjetsAdmin(admin.ModelAdmin):
    fields = ('name', 'slug', 'description', 'image')
    readonly_fields = ('slug',)

    list_display = ('name', 'short_description', 'ordre',)
    list_editable = ('ordre',)
    list_display_links = ('name',)
    list_filter = ('name',)
    search_fields = ('name', 'description')
    ordering = ('ordre',)

    inlines = (ProjetPagesAdmin, )
