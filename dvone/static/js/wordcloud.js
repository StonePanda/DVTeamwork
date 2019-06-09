var chart = echarts.init(document.getElementById('main2'));

            var option = {
                tooltip: {},
                series: [ {
                    type: 'wordCloud',
                    gridSize: 2,
                    sizeRange: [12, 50],
                    rotationRange: [-90, 90],
                    shape: 'pentagon',
                    width: 600,
                    height: 400,
                    drawOutOfBound: true,
                    textStyle: {
                        normal: {
                            color: function () {
                                return 'rgb(' + [
                                    Math.round(Math.random() * 160),
                                    Math.round(Math.random() * 160),
                                    Math.round(Math.random() * 160)
                                ].join(',') + ')';
                            }
                        },
                        emphasis: {
                            shadowBlur: 10,
                            shadowColor: '#333'
                        }
                    },
                    data: []
                } ]
            };
            chart.showLoading();
            //var cloud = [];

            $.ajax({
                type : "get",
                async : true,
                url : "https://easy-mock.com/mock/5cd9787f81f5e5576a8643d4/example/cloud",
               // data: {},
                dataType : "json",
                success : function(data){
                    console.log(data);
                   // var obj = JSON.parse(data);
                    //console.log(obj);
                   // for(var i = 0; i < data.length; i++){
                        //cloud.push(data[i]);
                    //}
                    chart.hideLoading();
                    chart.setOption({
                        series: [{
                            data: data
                        }]
                    })
                },
                error: function(errorMsg){
                    alert("图标请求数据失败");
                    chart.hideLoading();
                }

            })

            chart.setOption(option);

            window.onresize = chart.resize;