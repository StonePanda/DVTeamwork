//% load static %}
var mychart2=echarts.init(document.getElementById("main2"));
var mychart3=echarts.init(document.getElementById("main3"));
//var colorlist=["#da0d68","#e0719c","#f99e1c","#ef5a78","#f99e1c"]
var option2 = {
    /*title: {
        text: 'SUNBURST',
        textStyle: {
            fontSize: 14,
            align: 'center'
        },
        subtextStyle: {
            align: 'center'
        }
    },*/
   // center: ["20%", "50%"],
   //color: colorlist,
   tooltip: {
        trigger: "item"

   },
    series: [{
        type: 'sunburst',
        highlightPolicy: 'ancestor',
        data: [],
        radius: [0, '95%'],
        sort: null,

        levels: [{}, {
            r0: '0',
            r: '25%',
            itemStyle: {
                borderWidth: 2
            },
            label: {
                rotate: 'tangential'
            }
        }, {
            r0: '25%',
            r: '55%',
            label: {
                align: 'center'
            }
        }, {
            r0: '55%',
            r: '90%',
            label: {
                align: 'right'
            },
            itemStyle: {
                borderWidth: 3
            }
        }]
    }/*,
    {
        type:"scatter",
        data:[0,0],
        symbolSize:1,
        label: {
            normal: {
                show: true,
                formatter: "9.5",
                fontSize: 20,
                color: "#000"
            }
        }
    }*/]
};
mychart2.showLoading();
            //sunburst异步获取数据
            $.ajax({
                type : "get",
                async : true,
                url : "http://127.0.0.1:8000/views/view2",
               // data: {},
                dataType : "json",
                success : function(data){
                    //console.log(data);
                   // var obj = JSON.parse(data);
                    //console.log(obj);
                   // for(var i = 0; i < data.length; i++){
                        //cloud.push(data[i]);
                    //}
                    mychart2.hideLoading();
                    mychart2.setOption({
                        series: [{
                            data: data
                        }]
                    })

                },
                error: function(errorMsg){
                    alert("图标请求数据失败");
                    mychart2.hideLoading();
                }

            })

            mychart2.setOption(option2);
            var option3 = {//云图
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
            
            //cloud-world get data
            mychart3.showLoading();
            $.ajax({
                type: "get",
                async : true,
                url: "http://127.0.0.1:8000/views/view4",
                dataType: "json",
                success:function(data){
                    mychart3.hideLoading();
                    mychart3.setOption({
                        series:[{
                            data: data
                        }]
                    })

                },
                error:function(errorMsg){
                    alert("请求数据失败！");
                    mychart3.hideLoading();
                }
            })
            mychart3.setOption(option3);

            $.ajax({
                type: "get",
                async : true,
                url: "http://127.0.0.1:8000/views/view3",
                dataType:"json",
                success: function(data){
                        $.each(data,function(i, item){
                            $("#name"+i).text(""+ item.commenter + "");
                            $("#raty"+i).raty({
                                path:"http://127.0.0.1:8000/static/img",
                                score:item.raty,
                                readOnly:true
                            });
                            $("#comment"+i).text("" + item.comment + "");
                        });
                },
                error:function(errorMsg){
                    alert("获取数据失败");
                }
            })

            //点击星级实现交互
mychart2.on('click',function (params) {
    //console.log(params.componentType);
    //console.log(params.name);
    // 控制台打印数据的名称
    if (params.componentType === 'series'){

        if(params.name == "五星"){
            mychart3.showLoading();
            $.ajax({
                type : "get",
                async : true,
                url : "http://127.0.0.1:8000/views/view45",
               // data: {},
                dataType : "json",
                success : function(data){
                    //console.log(data);
                   // var obj = JSON.parse(data);
                    //console.log(obj);
                   // for(var i = 0; i < data.length; i++){
                        //cloud.push(data[i]);
                    //}
                    mychart3.hideLoading();
                    mychart3.setOption({
                        series: [{
                            data: data
                        }]
                    })
                },
                error: function(errorMsg){
                    alert("图标请求数据失败");
                    mychart3.hideLoading();
                }

            })

            mychart3.setOption(option3);
            //评论区数据的异步获取
            
            $.ajax({
                type :"get",
                async :true,
                url : "http://127.0.0.1:8000/views/view35",
                dataType : "json",
                success : function(data){
                    //清空数据
                    $("#name").empty();
                    $("#raty").empty();
                    $("#comment").empty();
                    //console.log(data);
                        $.each(data,function(i, item){
                            $("#name"+i).text(""+ item.commenter + "");
                            $("#raty"+i).raty({
                                path:"http://127.0.0.1:8000/static/img",
                                score:5,
                                readOnly:true
                            });
                            $("#comment"+i).text("" + item.comment + "");
                        });

                },
                error:function(errorMsg){
                    alert("图标请求数据失败");
                }
            })
        }
        else if(params.name == "四星"){
            //console.log("4星");

            //var cloud = [];
            mychart3.showLoading();
            $.ajax({
                type : "get",
                async : true,
                url : "http://127.0.0.1:8000/views/view44",
               // data: {},
                dataType : "json",
                success : function(data){
                    //console.log(data);
                   // var obj = JSON.parse(data);
                    //console.log(obj);
                   // for(var i = 0; i < data.length; i++){
                        //cloud.push(data[i]);
                    //}
                    mychart3.hideLoading();
                    mychart3.setOption({
                        series: [{
                            data: data
                        }]
                    })
                },
                error: function(errorMsg){
                    alert("图标请求数据失败");
                    mychart3.hideLoading();
                }

            })

            mychart3.setOption(option3);
            $.ajax({
                type :"get",
                async :true,
                url : "http://127.0.0.1:8000/views/view34",
                dataType : "json",
                success : function(data){
                    //清空数据
                    $("#name").empty();
                    $("#raty").empty();
                    $("#comment").empty();
                   // console.log(data);
                        $.each(data,function(i, item){
                            $("#name"+i).text(""+ item.commenter + "");
                            $("#raty"+i).raty({
                                path:"http://127.0.0.1:8000/static/img",
                                score:4,
                                readOnly:true
                            });
                            $("#comment"+i).text("" + item.comment + "");
                        });

                },
                error:function(errorMsg){
                    alert("图标请求数据失败");
                }
            })
        }
        else if(params.name == "三星"){
            //console.log("4星");

            //var cloud = [];
            mychart3.showLoading();
            $.ajax({
                type : "get",
                async : true,
                url : "http://127.0.0.1:8000/views/view43",
               // data: {},
                dataType : "json",
                success : function(data){
                   // console.log(data);
                   // var obj = JSON.parse(data);
                    //console.log(obj);
                   // for(var i = 0; i < data.length; i++){
                        //cloud.push(data[i]);
                    //}
                    mychart3.hideLoading();
                    mychart3.setOption({
                        series: [{
                            data: data
                        }]
                    })
                },
                error: function(errorMsg){
                    alert("图标请求数据失败");
                    mychart3.hideLoading();
                }

            })

            mychart3.setOption(option3);
            $.ajax({
                type :"get",
                async :true,
                url : "http://127.0.0.1:8000/views/view33",
                dataType : "json",
                success : function(data){
                    //清空数据
                    $("#name").empty();
                    $("#raty").empty();
                    $("#comment").empty();
                    //console.log(data);
                        $.each(data,function(i, item){
                            $("#name"+i).text(""+ item.commenter + "");
                            $("#raty"+i).raty({
                                path:"http://127.0.0.1:8000/static/img",
                                score:3,
                                readOnly:true
                            });
                            $("#comment"+i).text("" + item.comment + "");
                        });

                },
                error:function(errorMsg){
                    alert("图标请求数据失败");
                }
            })
        }
        else if(params.name == "二星"){
            //console.log("4星");

            //var cloud = [];
            mychart3.showLoading();
            $.ajax({
                type : "get",
                async : true,
                url : "http://127.0.0.1:8000/views/view42",
               // data: {},
                dataType : "json",
                success : function(data){
                   // console.log(data);
                   // var obj = JSON.parse(data);
                    //console.log(obj);
                   // for(var i = 0; i < data.length; i++){
                        //cloud.push(data[i]);
                    //}
                    mychart3.hideLoading();
                    mychart3.setOption({
                        series: [{
                            data: data
                        }]
                    })
                },
                error: function(errorMsg){
                    alert("图标请求数据失败");
                    mychart3.hideLoading();
                }

            })

            mychart3.setOption(option3);
            $.ajax({
                type :"get",
                async :true,
                url : "http://127.0.0.1:8000/views/view32",
                dataType : "json",
                success : function(data){
                    //清空数据
                    $("#name").empty();
                    $("#raty").empty();
                    $("#comment").empty();
                    //console.log(data);
                        $.each(data,function(i, item){
                            $("#name"+i).text(""+ item.commenter + "");
                            $("#raty"+i).raty({
                                path:"http://127.0.0.1:8000/static/img",
                                score:2,
                                readOnly:true
                            });
                            $("#comment"+i).text("" + item.comment + "");
                        });

                },
                error:function(errorMsg){
                    alert("图标请求数据失败");
                }
            })
        }
        else if(params.name == "一星"){
            //console.log("4星");

            //var cloud = [];
            mychart3.showLoading();
            $.ajax({
                type : "get",
                async : true,
                url : "http://127.0.0.1:8000/views/view41",
               // data: {},
                dataType : "json",
                success : function(data){
                   // console.log(data);
                   // var obj = JSON.parse(data);
                    //console.log(obj);
                   // for(var i = 0; i < data.length; i++){
                        //cloud.push(data[i]);
                    //}
                    mychart3.hideLoading();
                    mychart3.setOption({
                        series: [{
                            data: data
                        }]
                    })
                },
                error: function(errorMsg){
                    alert("图标请求数据失败");
                    mychart3.hideLoading();
                }

            })

            mychart3.setOption(option3);
            $.ajax({
                type :"get",
                async :true,
                url : "http://127.0.0.1:8000/views/view31",
                dataType : "json",
                success : function(data){
                    //清空数据
                    $("#name").empty();
                    $("#raty").empty();
                    $("#comment").empty();
                    //console.log(data);
                        $.each(data,function(i, item){
                            $("#name"+i).text(""+ item.commenter + "");
                            $("#raty"+i).raty({
                                path:"http://127.0.0.1:8000/static/img",
                                score:1,
                                readOnly:true
                            });
                            $("#comment"+i).text("" + item.comment + "");
                        });

                },
                error:function(errorMsg){
                    alert("图标请求数据失败");
                }
            })
        }
    }
    
});