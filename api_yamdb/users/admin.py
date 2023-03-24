from django.contrib import admin

from users.models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'name',
                    'email',
                    'role',
                    'bio',
                    'first_name',
                    'last_name',
                    )
    list_display_links = ('id', 'name', 'role',)
    search_fields = ('first_name', 'last_name',)
    list_filter = ('first_name', 'last_name', 'role',) 


admin.site.register(CustomUser, CustomUserAdmin)
