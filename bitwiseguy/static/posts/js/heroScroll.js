$(document).ready(function(){
	$(window).scroll(function(){
		if($(document).scrollTop() > 10){
		$('.hero').addClass('shrink');
	}
		else{
		$('.hero').removeClass('shrink');

		}
	});
});
