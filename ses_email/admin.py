from django.contrib import admin

from .models import VerificationCode


# Register your models here.
admin.site.site_title = 'General API'
admin.site.site_header = 'General API'
admin.site.index_title = 'General API Models'


class VerificationCodeAdmin(admin.ModelAdmin):
    empty_value_display = 'None'
    list_display = ('code', 'validity', 'rate_limit', 'created_at',)
    list_filter = ('validity', 'created_at',)


admin.site.register(VerificationCode, VerificationCodeAdmin)
