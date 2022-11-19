from django.contrib import admin
from .models import Marble, Category
# Register your models here.


class MarbleAdmin(admin.ModelAdmin):
    list_display = ("title","is_home","is_active","slug")
    list_editable =("is_home","is_active",)
    search_fields = ("title","description",)
    readonly_fields = ("slug",)
    list_filter=("category","is_active","is_home")
    
    
admin.site.register(Marble,MarbleAdmin)
admin.site.register(Category)