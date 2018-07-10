from django.contrib import admin

from .models import SiteModel, SiteDataModel


@admin.register(SiteModel)
class SiteAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )


@admin.register(SiteDataModel)
class SiteDataAdmin(admin.ModelAdmin):
    list_display = ('site', 'a_value', 'b_value', )
