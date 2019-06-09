var mychart1=echarts.init(document.getElementById('main1'));
var option={
	tooltip : {
            trigger: 'item',
            formatter: "{a} <br/>{b} : {c}"
        },
    calculable : true,
    legend : {
    	data : [],
    	x: 20
    },
    grid: [
        {x: '5%', y: '7%',width: "45%"},
        {x: '50%', y: '7%',width:"45%"}
    ],
    xAxis: [{
    		gridIndex: 0, 
        	type:"category",
        	data:[],
       	    inverse:true,
        	splitLine:{
            	show:false
        	}
        },
        {
        	gridIndex: 1,
        	type:"category",
        	data:[],
        	splitLine:{
            show:false
        }
    }
    ],
    yAxis: [{
    		gridIndex: 0,
    		min: 0,
    		max: 100,
    		axisLabel:{
            	show:false
        },
        position: "right"
    },
        {
        	name: "分数",
        	gridIndex: 1,
        	min: 0,
        	max: 100
        }
    ],
     dataZoom: [
       {
            show: true,
            start: 0,
            end: 100,
            xAxisIndex: 0
        },
        {
            type: 'inside',
            start: 0,
            end: 100,
            xAxisIndex: 0
        },
        {
            show: true,
            start:0,
            end: 100,
            xAxisIndex: 1
        },
        {
        	type: "inside",
        	start: 0,
        	end: 100,
        	xAxisIndex: 1
        }
    ],
   
    series : [
    	{
    		name : "戏剧",
    		yAxisIndex: 0,
    		xAxisIndex: 0,
    		type : "bar",
    		data :[]
           
    	},
    	{
    		name : "剧情",
    		type : "bar",
    		yAxisIndex: 1,
    		xAxisIndex: 1,
    		data :[]
    	},
    ]
    
}
mychart1.showLoading();
$.ajax({
	type: "get",
	async: true,
	url: "http://127.0.0.1:8000/views/view1",
	dataType: "json",
	success: function(data){
		mychart1.hideLoading();
		//console.log(data[0].type);
		//console.log(data.mark);
		var type = [data.data[0].type,data.data[1].type];
        //var coord = data.mark;
		mychart1.setOption({
			legend:{
				data: type
			},
			xAxis: [{
				gridIndex:0,
				data: data.data[0].moviename
			},
			{
				gridIndex: 1,
				data: data.data[1].moviename

			}],
             
			series : [
    	{
    		name : data.data[0].type,
    		yAxisIndex: 0,
    		xAxisIndex: 0,
    		type : "bar",
    		data : data.data[0].data,
            markPoint:{
                
                data:[{
                    name: data.mark[0][0],
                    value: data.mark[0][1],
                    coord:data.mark[0],
                    label:{
                        show:true,
                        formatter: data.mark[0][0]
                    }
                }]
            }
    	},
    	{
    		name : data.data[1].type,
    		type : "bar",
    		yAxisIndex: 1,
    		xAxisIndex: 1,
    		data :data.data[1].data,
            markPoint:{
                
                data:[{
                    name: data.mark[1][0],
                    value: data.mark[1][1],
                    coord:data.mark[1],
                    label:{
                        show:true,
                        formatter: data.mark[1][0]
                    }
                }]
            },
    	}
    ]
		});
	}
})

mychart1.setOption(option);
