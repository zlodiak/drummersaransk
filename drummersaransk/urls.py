from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('drummersaransk',
	url(r'^accounts/logout/$', 'views.logout', name='logout', ),	
	url(r'^accounts/login/$', 'views.login', name='login', ),
	url(r'^accounts/loggedin/$', 'views.loggedin', ),
	url(r'^accounts/invalid_login/$', 'views.invalid_login', ),
	
	url(r'^accounts/registration/$', 'views.registration', name='registration', ),
	url(r'^accounts/registration_success/$', 'views.registration_success', ),		
	
	url(r'^userprofile/friends_search/$', 'views.friends_search', name='friends_search', ),
	
	url(r'^userprofile/friends_list_edit/$', 'views.friends_list_edit', name='friends_list_edit', ),
	url(r'^userprofile/friends_list_edit/(?P<friend_id>[0-9]*)/$', 'views.friends_list_edit', name='friends_list_edit', ),
			
	url(r'^userprofile/password_page/$', 'views.password_page', name='password_page', ),		
	url(r'^userprofile/password_page_changed/$', 'views.password_page_changed', ),	
		
	url(r'^userprofile/avatar_page/$', 'views.avatar_page', name='avatar_page', ),		
	url(r'^userprofile/avatar_page_changed/$', 'views.avatar_page_changed', ),	
		
	url(r'^userprofile/personal_data_page/$', 'views.personal_data_page', name='personal_data_page', ),		
	url(r'^userprofile/personal_data_page_changed/$', 'views.personal_data_page_changed', ),
	
	url(r'^userprofile/drum_data_page/$', 'views.drum_data_page', name='drum_data_page', ),		
	url(r'^userprofile/drum_data_page_changed/$', 'views.drum_data_page_changed', name='drum_data_page_changed', ),	
			
	url(r'^userprofile/path_glory_edit/$', 'views.path_glory_edit', name='path_glory_edit', ),		
	url(r'^userprofile/path_glory_add_item/$', 'views.path_glory_add_item', name='path_glory_add_item', ),		
	url(r'^userprofile/path_glory_edit/(?P<id>[0-9]+)/$', 'views.path_glory_edit_item', name='path_glory_edit_item', ),		
	url(r'^userprofile/path_glory_edit_item_changed/$', 'views.path_glory_edit_item_changed', name='path_glory_edit_item_changed', ),		
	url(r'^userprofile/path_glory_add_item_added/$', 'views.path_glory_add_item_added', name='path_glory_add_item_added', ),		
						
	url(r'^(?P<id>[0-9]+)/$', 'views.user_personal', name='user_personal', ),
	url(r'^(?P<id>[0-9]+)/druminfo/$', 'views.user_druminfo', name='user_druminfo', ),
	url(r'^(?P<id>[0-9]+)/path_glory/$', 'views.path_glory', name='path_glory', ),	
	url(r'^(?P<id>[0-9]+)/path_glory/(?P<id_p>[0-9]+)/$', 'views.user_path_glory_page', name='user_path_glory_page', ),
	url(r'^(?P<id>[0-9]+)/friends_list/$', 'views.user_friends_list', name='user_friends_list', ),
	
	url(r'^captcha/', include('captcha.urls')),
	url(r'^admin/', include(admin.site.urls)),	
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )


urlpatterns += patterns('drummersaransk',
	url(r'^$', 'views.index', ),
	url(r'^index/', 'views.login', ),
	url(r'^page_error404/', 'views.page_error404', ),
	url(r'^None/', 'views.login', ),	
	url(r'^.*/', 'views.page_error404', ),
)
   
   
if settings.DEBUG:
	import debug_toolbar
	urlpatterns += patterns('',
		url(r'^__debug__/', include(debug_toolbar.urls)),
	)   

