$(document).ready(function(){
	// 构建导航栏
	$("#nav").html('<nav class="navbar navbar-fixed-top my-navbar" role="navigation"><div class="container-fluid"><div class="navbar-header"><a class="navbar-brand" href="./"><span class="glyphicon glyphicon-film"></span>&nbsp;&nbsp;疾风电影数据</a></div><div><ul class="nav navbar-nav"><li class="active"><a href="./"><span class="glyphicon glyphicon-home"></span>&nbsp;&nbsp;首页</a></li><li><a href="./movielist"><span class="glyphicon glyphicon-list"></span>&nbsp;&nbsp;电影列表</a></li><li><a href="./moviechart"><span class="glyphicon glyphicon-stats"></span>&nbsp;&nbsp;图表展示</a></li><li><a href="./version"><span class="glyphicon glyphicon-list-alt"></span>&nbsp;&nbsp;版本日志</a></li><li><a href="#" onclick="alert(\'个人邮箱：1402808108@qq.com\');"><span class="glyphicon glyphicon-phone-alt"></span>&nbsp;&nbsp;联系我们</a></li></ul></div></div></nav>');
	// 页面滚动触发改变导航栏背景事件
	$(window).scroll(function () {
		if ($(".navbar").offset().top > 50) {
			$(".navbar-fixed-top").addClass("top-nav");  
		}else {
			$(".navbar-fixed-top").removeClass("top-nav");
		}
	});
});