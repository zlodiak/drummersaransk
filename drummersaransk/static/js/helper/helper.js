$(document).ready(function(){
	////dynamic header height
	function headerHeightChange(){
		var	headerHeight = $('.navbar').outerHeight();
		var	newHeaderHeight = headerHeight;
		
		$('body > .container').css({
			'padding-top': newHeaderHeight + 'px',
		});
	}
	
	headerHeightChange();
	
	$(window).resize(function(){
		headerHeightChange();
	});
	
	////active menu punkt
	var	pathname = location.pathname;
	var	pathnameList = pathname.split('/');
	var	slug1 = '/' + pathnameList[1];
	var	slug2 = '/' + pathnameList[2];

	//console.log('pathname::' + pathname);
	//console.log('pathnameList::' + pathnameList);
	//console.log('slug1::' + slug1);
	//console.log('slug1::' + slug2);
	//console.log('slug1 + slug2 + slash::' + slug1 + slug2 + '/');

	$('.nav_edit a').each(function(){
		var	href = $(this).attr('href');
		
		$(this).closest('li').removeClass('active');
		
		if(href == slug1 + slug2 + '/'){
			$(this).closest('li').addClass('active');
		}
	});	
	
	$('.nav_basic a').each(function(){
		var	href = $(this).attr('href');
		
		$(this).closest('li').removeClass('active');
		
		if(href == slug1 + slug2 + '/'){
			$(this).closest('li').addClass('active');
		}
		else if(slug2 == '/'){
			$('li').eq(0).addClass('active');
		}
	});	

	////techer_fio
	var teacher_fio_elem = $('#teacher_fio');
	var id_teacher_fio_elem = $('#id_teacher_fio');	
	var	selected_num = $("#id_teacher :selected").val();
	
	if(selected_num == 2){
		teacher_fio_elem.removeClass('hide');
	};
	
	$('#id_teacher').on('change', function(){		
		$(this).find("option:selected").each(function(){
			num = $(this).val();
		});	
		
		//console.log(num);
		
		if(num == 2){
			teacher_fio_elem.removeClass('hide');
		}
		else{
			//console.log('else');
			teacher_fio_elem.addClass('hide');
			id_teacher_fio_elem.val('');
		}
	});
});