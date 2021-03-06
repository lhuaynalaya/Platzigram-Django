# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from users.models import Profile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from django.contrib.auth.models import User
from users.models import Profile
from posts.models import Post

# Register your models here.
#admin.site.register(Profile)
@admin.register(Profile)

class ProfileAdmin(admin.ModelAdmin):
	list_display = ('pk', 'user', 'phone_numer', 'website', 'picture')
	list_display_links = ('pk', 'user')
	list_editable = ('phone_numer', 'website')
	search_fields = ('user__email', 'user__username', 'user__first_name', 'user__last_name', 'phone_numer')
	list_filter = ('user__is_active', 'user__is_staff', 'created', 'modified')

	fieldsets = (
		('Profile', {
			'fields': (('user', 'picture'),),
		}),
		('Extra info', {
			'fields': (
				('website', 'phone_numer'),
				('biography')
			)
		}),
		('Metadata', {
			'fields': (('created', 'modified'))
		})
	)

	readonly_fields = ('created', 'modified')

class ProfileInline(admin.StackedInline):
	model = Profile
	can_delete = False
	verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
	inlines = (ProfileInline,)
	list_display = (
		'username',
		'email',
		'first_name',
		'last_name',
		'is_active',
		'is_staff'
	)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)


@admin.register(Post)

class ProfileAdmin(admin.ModelAdmin):
	list_display = ('pk', 'user', 'profile', 'title', 'photo')
	list_display_links = ('pk', 'user')
	list_editable = ('title', 'photo')
	search_fields = ('profile', 'title', 'user')

	readonly_fields = ('created', 'modified')
