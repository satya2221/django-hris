from django.contrib import admin
from .models import Profile

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at') # bisa pilih apa saja yang akan ditampilkan

admin.site.register(Profile, ProfileAdmin)
# Register your models here.
