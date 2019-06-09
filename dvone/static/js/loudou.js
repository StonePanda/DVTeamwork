var mychart1 = echarts.init(document.getElementById("main1"));
option = {
    /*title: {
        text: '漏斗图',
        left: 'left',
        top: 'bottom'
    },*/
    tooltip: {
        trigger: 'item',
        formatter: "{a} <br/>{b} : {c}%"
    },
    /*toolbox: {
        show: true,
        orient: 'vertical',
        top: 'center',
        feature: {
            dataView: {readOnly: false},
            restore: {},
            saveAsImage: {}
        }
    },
    legend: {
        orient: 'vertical',
        left: 'left',
        data: []
    },*/
    calculable: true,
    series: [
        {
            name: '漏斗图',
            type: 'funnel',
            width: '40%',
            height: '45%',
            left: '25%',
            top: '50%',
            funnelAlign: 'center',
           // color: "rgb(145,199,174)",

            center: ['25%', '25%'],  // for pie
            label:{
                show: false,
                /*normal:{
                    position: "top"
                }*/
            },

            data:[]
        },
        {
            name: '金字塔',
            type:'funnel',
            width: '40%',
            height: '45%',
            left: '25%',
            top: '5%',
            sort: 'ascending',
            funnelAlign: 'center',
            //color: "rgb(212,130,101)",

            center: ['25%', '75%'],  // for pie
            label: {
                show: false,
                /*normal: {
                    position: 'top'
                }*/
            },

            data:[]
        }
    ]
};
mychart1.showLoading();
$.ajax({
    type: "get",
    async: true,
    url:"https://easy-mock.com/mock/5cd9787f81f5e5576a8643d4/example/lou",
    dataType: "json",
    success: function(data){
        mychart1.hideLoading();
        mychart1.setOption({
            /*legend: {
                data: data.name
            },*/
            series: [{
                name: "漏斗图",
                data:data.data1
            },
            {
                name:"金字塔",
                data:data.data2
            }]
        })

    },
    error:function(errorMsg){
        alert("图标请求数据失败");
        mychart1.hideLoading();

    }
})


mychart1.setOption(option);
