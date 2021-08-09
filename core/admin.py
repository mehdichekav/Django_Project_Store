from django.contrib import admin
from .models import BaseModel


# @admin.register(BaseModel)
# class CoreAdmin(admin.ModelAdmin):
#     list_display = ('log_delete', 'is_expired', )
#
#     def log_delete(self, request, queryset):
#         rows = queryset.update(True)
#         self.rows = True
#         self.save()
#
#     admin.site.add_action(log_delete)



