from django.contrib import admin
# from .forms import RegisterForm
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username','email','phone')
    search_fields = ('username','email','phone')
    ordering = ('username',)
    
admin.site.register(CustomUser,CustomUserAdmin)

# Register your models here.
