$(document).ready(function(){

	var mydate = new Date();
	var datestr = mydate.getFullYear() + " 年 " + (mydate.getMonth()+1) + " 月 " + mydate.getDate() + " 日 " + mydate.getHours() + " 点 ";
	
	var name1 = "实时票房：万元（人民币）";
	var name2 = "累计票房：万元（人民币）";
	var name3 = "豆瓣评分";
	var name4 = "时光网评分";
	var xdata1 = [], series1 = [];
	var xdata2 = [], series2 = [];
	var xdata3 = [], series3 = [];
	var xdata4 = [], series4 = [];
	
	var mybar1 = creatbar("chart1", datestr, name1);
	var mybar2 = creatbar("chart2", datestr, name2);
	var mybar3 = creatbar("chart3", datestr, name3);
	var mybar4 = creatbar("chart4", datestr, name4);
	
	$.ajax({
		type: 'POST',
		url: '/getmoviepiaofang',
		data: {"param":"boxoffice","isnum":"True"},
		success: function(result){
			var jsondata = eval('(' + result + ')');
			xdata1 = jsondata.key;
			series1 = jsondata.value;
			showbar(mybar1, xdata1, series1, name1);
		}
	});
	
	$.ajax({
		type: 'POST',
		url: '/getmoviepiaofang',
		data: {"param":"allboxoffice","isnum":"True"},
		success: function(result){
			var jsondata = eval('(' + result + ')');
			xdata2 = jsondata.key;
			series2 = jsondata.value;
			showbar(mybar2, xdata2, series2, name2);
		}
	});
	
	$.ajax({
		type: 'POST',
		url: '/getmoviepiaofang',
		data: {"param":"douban","isnum":"True"},
		success: function(result){
			var jsondata = eval('(' + result + ')');
			xdata3 = jsondata.key;
			series3 = jsondata.value;
			showbar(mybar3, xdata3, series3, name3);
		}
	});

	$.ajax({
		type: 'POST',
		url: '/getmoviepiaofang',
		data: {"param":"mtime","isnum":"True"},
		success: function(result){
			var jsondata = eval('(' + result + ')');
			xdata4 = jsondata.key;
			series4 = jsondata.value;
			showbar(mybar4, xdata4, series4, name4);
		}
	});
	
	$(window).scroll(function () {
		if ($(window).scrollTop() >= $('.panel').height() * 1 && $(window).scrollTop() <= $('.panel').height() * 2) {
			showbar(mybar1, xdata1, series1, name1);
		}else{
			clearbar(mybar1, name1);
		}
		
		if ($(window).scrollTop() >= $('.panel').height() * 2 && $(window).scrollTop() <= $('.panel').height() * 3) {
			showbar(mybar2, xdata2, series2, name2);
		}else{
			clearbar(mybar2, name2);
		}

		if ($(window).scrollTop() >= $('.panel').height() * 3 && $(window).scrollTop() <= $('.panel').height() * 4) {
			showbar(mybar3, xdata3, series3, name3);
		}else{
			clearbar(mybar3, name3);
		}

		if ($(window).scrollTop() >= $('.panel').height() * 4 && $(window).scrollTop() <= $('.panel').height() * 5) {
			showbar(mybar4, xdata4, series4, name4);
		}else{
			clearbar(mybar4, name4);
		}
	});
});

function creatbar(id, datestr, name){

	// 基于准备好的dom，初始化echarts实例
    var mybar = echarts.init(document.getElementById(id));
    
	// 指定图表的配置项和数据
    var option = {
        title: {
            text: '疾 风 电 影 数 据 - ' + datestr,
            textStyle: {color: '#00bfff'}
        },
        tooltip: {},
        legend: {
            data:[
            	{
            		name: name,
            		textStyle: {color: '#00bfff'},
            	},
            ],
        },
        xAxis: {
            data: [],
            splitLine:{show: false},
            axisLine: {
            	lineStyle:{color:'#00bfff'}
            },
            axisLabel: {
            	interval:0,
            	rotate: 20,
            }
        },
        yAxis: {
        	splitLine:{show: false},
        	axisLine: {lineStyle:{color:'#00bfff'}}
        },
        series: [
        	{
	            name: name,
	            type: 'bar',
	            data: [],
	            color: '#00bfff',
		        label: {
					normal: {
						show: true,
						position: 'top',
						textStyle: {color: '#00bfff'},
					},
				},
        	},
        ],
    };
    
    // 使用刚指定的配置项和数据显示图表。
    mybar.setOption(option);
    
    return mybar;
}

function showbar(mybar, xdata, series, name){
	mybar.setOption({
		xAxis: {
            data: xdata
        },
        series: [{
            name: name,
            data: series
        }]
	});
}

function clearbar(myChart, name){
	// 清空图表
	myChart.setOption({
		xAxis: {
            data: []
        },
        series: [{
            name: name,
            data: []
        }]
	});
}

$(function(){
	$.scrollify({
		section: '.bg'
	});
});
