from django.contrib import admin
from .models import Department, DepartmentMember

# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at') # bisa pilih apa saja yang akan ditampilkan
    list_filter = ('created_at', 'updated_at', 'is_active') # memunculkan menu filter di kanan admin
    search_fields = ('name',)

class DepartmentMemberAdmin(admin.ModelAdmin):
    list_display = ('department','created_at', 'updated_at',)

admin.site.register(Department, DepartmentAdmin)
admin.site.register(DepartmentMember, DepartmentMemberAdmin)