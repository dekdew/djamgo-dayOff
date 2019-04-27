from django.contrib import admin

from django.contrib.auth.models import Permission

from dayOff.models import DayOff

admin.site.register(Permission)


class DayOffAdmin(admin.ModelAdmin):
  list_display = ['id', 'create_by', 'reason', 'date_start', 'date_end', 'approve_status']
  readonly_fields = ['create_by', 'reason', 'date_start', 'date_end', 'type']
  search_fields = ['date_start', 'date_end', 'create_by__username', 'reason']

  fieldsets = [
    ('ข้อมูลการลา', {'fields': ['create_by', 'reason', 'date_start', 'date_end', 'type']}),
    ('การอนุมัติ', {'fields': ['approve_status']})
  ]


admin.site.register(DayOff, DayOffAdmin)
