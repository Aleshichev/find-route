from django.contrib import admin

from routes.models import Route



class RouteAdmin(admin.ModelAdmin):
    """редактирование админки"""
    class Meta:
        model = Route
    list_display = ('name', 'from_city', 'to_city', 'travel_times' )
    list_editable = ('travel_times',)


admin.site.register(Route, RouteAdmin)
