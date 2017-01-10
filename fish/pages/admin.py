from django.contrib import admin

# Register your models here.

from pages.models import WebPage


class WebPageAdmin(admin.ModelAdmin):
    list_display = ('url', 'links')


admin.site.register(WebPage, WebPageAdmin)
