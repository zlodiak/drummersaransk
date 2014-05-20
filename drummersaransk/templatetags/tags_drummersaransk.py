from django import template
from django.contrib.auth.models import User
from django.http import HttpResponse
import re

from drummersaransk.models import Friends, UserProfile
from drummersaransk.utils import compare_ids

register = template.Library()
    

@register.inclusion_tag("part_nav_edit.html")
def part_nav_edit(user, request):
	ids_data = compare_ids(request)
			
	return{
		'flag_homepage': ids_data['flag_homepage'],
		'user_pk': user.pk,
		'is_authenticated': user.is_authenticated,
	}
	
	
@register.inclusion_tag("part_nav_basic.html")
def part_nav_basic(user_pk, request):
	if 'cookie_user_pk' in request.COOKIES:
		user_pk = request.COOKIES['cookie_user_pk']
		
	search = re.search('^\/(?P<slug>[0-9]+?)\/.*', request.path)
	if search is not None:
		user_pk = search.group(1)	
		response = HttpResponse()
		response.set_cookie( 'cookie_user_pk', user_pk )
		
	if not request.user.is_authenticated():
		user_pk = 'index'
		
	return{
		'user_pk': user_pk,
		'is_authenticated': request.user.is_authenticated(),
	}
	
	
@register.inclusion_tag("part_auth_area.html")
def part_auth_area(is_authenticated):
	return {
		'is_authenticated': is_authenticated,
	}	
	
	
@register.inclusion_tag("auth_area_logged_in.html")
def logged_in(username):	
	return{
		'auth_name': username,
	}
	
	
@register.inclusion_tag("auth_area_logged_out.html")
def logged_out():	
	return	
	
	
@register.inclusion_tag("right_col.html")
def right_col():	
	return	
	
	
@register.inclusion_tag("part_friends_buttons_area.html")
def friends_buttons_area(request):	
	flag_friend = True

	ids_data = compare_ids(request)
			
	flag_friend = Friends.get_entry(user_id=request.user.pk, friend_id=ids_data['path_pk'])
				
	return {
		'flag_homepage': ids_data['flag_homepage'],
		'flag_friend': flag_friend,
	}	
	
	
@register.inclusion_tag("user_friend_item.html")
def friend_item(friend_id, flag_buttons_visibility):	
	try:
		user_info = UserProfile.objects.get(user_ptr_id=friend_id)
	except:
		return False
	else:
		return{
			'user_info': user_info,
			'flag_buttons_visibility': flag_buttons_visibility,
		}
	
	

