
var mychart4=echarts.init(document.getElementById("main4"));


var option1 = {
    /*title: {
        text: 'Punch Card',
    },*/
    /*legend: {
        data: ['Punch Card'],
        left: 'right'
    },*/
    tooltip: {
        position: 'top',
        formatter: function (params) {
            return "共获奖(含提名): "+ params.data[2] + "部";
        }

    },
    grid: {
        left: 25,
        bottom: 10,
        right: 20,
        containLabel: true
    },
    xAxis: {
        type: 'category',
        data: [],
        boundaryGap: false,
        splitLine: {
            show: true,
            lineStyle: {
                color: '#999',
                type: 'dashed'
            }
        },
        axisLine: {
            show: false
        }
    },
    yAxis: {
        type: 'category',
        data: [],
        splitLine: {
            show: true
        },
        axisLine: {
            show: false
        },
        axisLabel: {
            margin: 25
        }
    },
    series: [{
        name: 'Punch Card',
        type: 'scatter',
        symbolSize: function (val) {
            /*if (val[2]>7) {
                return 
            }*/
            if(val[2]==0)
                return 0
            return val[2] +4;
        },
        data: [],
        animationDelay: function (idx) {
            return idx * 8;
        }
    }]
};
	mychart4.showLoading();//加载下载动画

  /* function settooltip(params,price) {
                                 var str = "共获奖(含提名): "+ params.data[2] + "部" + "<br/>";
                                 for(var i = 0; i < price[params.data[0]][params.data[1]].length; i++){
                                    str += price[params.data[0]][params.data[1]][i];
                                    str += "<br/>";
                                 }
                                 return str;
                                }*/
	$.ajax({
		type : "get",
		async : true,
		url : "http://127.0.0.1:8000/views/view5",
		dataType : "json",
		success : function(data){
			//if(data.code == 'success'){
				/*var obj1 = JSON.parse(data.years);//解析后台传来的json数据
				var obj2 = JSON.parse(data.name);
				var obj3 = JSON.parse(data.data)
				for(var i = 0; i < data.years.length; i++){
					years.push(data.years[i]);
				}
				for(var i = 0; i < data.name.length; i++){
					name.push(data.name[i]);
				}
				for(var i = 0; i < data.data.length; i++){
					data1.push(data.data[i]);
				}*/


				mychart4.hideLoading();//隐藏加载动画
				mychart4.setOption({
				    tooltip: {
       					 	position: 'top',
       						formatter: function(params){
                                 var str = "共获奖(含提名): "+ params.data[2] + "部" + "<br/>";
                                 for(var i = 0; i < data.price[params.data[0]][params.data[1]].length; i++){
                                    str += data.price[params.data[0]][params.data[1]][i];
                                    str += "<br/>";
                                 }
                                 return str;
                            }
   							},
					xAxis : {
						data : data.years
					},
					yAxis : {
						data : data.name
					},
					series: [{
						name: 'Punch Card',
						data : data.data
					}]
				});


				
			//}

			//else{
					//alert("failed");
			//}
			

		},
		error : function(errorMsg){
				alert("图标请求数据失败");
				mychart4.hideLoading();
			}


	})
	mychart4.setOption(option1);