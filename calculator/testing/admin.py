from django.contrib import admin
from .models import Testing

# Register your models here.
# admin.site.register(Testing)

class MemberAdmin(admin.ModelAdmin):
  list_display = ("name", "phone")

admin.site.register(Testing, MemberAdmin)