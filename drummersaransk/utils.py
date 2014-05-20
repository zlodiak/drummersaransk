import re

def compare_ids(request):
	flag_homepage = False
	path_pk = ''
	
	search = re.search('^\/(?P<slug>[0-9]+?)\/.*', request.path)
	if search is not None:
		path_pk = search.group(1)	
		
		if str(path_pk) != str(request.user.pk):
			flag_homepage = True		

	return{
		'flag_homepage': flag_homepage,
		'path_pk': path_pk,
	}
