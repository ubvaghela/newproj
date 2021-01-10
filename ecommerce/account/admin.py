# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import User,State,City,UserProfile,SellerProfile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group


admin.site.register(State)
admin.site.register(UserProfile)
admin.site.register(SellerProfile)


class CityAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'state_id')
    list_filter = ('state_id',)
    search_fields = ('name',)
    ordering = ('state_id',)

admin.site.register(City,CityAdmin)


class UserAdmin(BaseUserAdmin):
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

admin.site.register(User,UserAdmin)
admin.site.unregister(Group)