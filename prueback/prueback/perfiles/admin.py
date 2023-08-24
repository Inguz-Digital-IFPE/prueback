from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'nombre', 'apellidos', 'curp',
                    'fecha_nacimiento', 'edad')
    list_filter = ('user',)
    search_fields = ('user__username', 'nombre', 'apellidos', 'curp')
    fieldsets = (
        (None, {
            'fields': ('user', 'nombre', 'apellidos', 'curp')
        }),
        ('Información Adicional', {
            'fields': ('fecha_nacimiento', 'edad')
        }),
    )
    ordering = ('user__username',)


admin.site.register(UserProfile, UserProfileAdmin)