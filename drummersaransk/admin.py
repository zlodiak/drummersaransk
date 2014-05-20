from django.contrib import admin
from drummersaransk.models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
	fields = ['family', 'name1', 'name2', 'nickname', 'gender', 'status', 'city', 'phone', 'skype', 'email', 'other', 'avatar', ]	
	list_display = ['nickname', 'email']
	search_fields = ['nickname', ]
	
	class Meta:
		verbose_name = 'Профиль пользователя'
		verbose_name_plural = 'Профиль пользователя'		

	
admin.site.register(UserProfile, UserProfileAdmin)

