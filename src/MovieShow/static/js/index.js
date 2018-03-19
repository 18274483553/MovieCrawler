$(document).ready(function(){
	// 页面滚动触发改变导航栏背景事件
	$(window).scroll(function () {
		if ($(".navbar").offset().top > 50) {
			$(".navbar-fixed-top").addClass("top-nav");  
		}else {
			$(".navbar-fixed-top").removeClass("top-nav");
		}
	});
});
