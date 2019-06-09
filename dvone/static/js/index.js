function
gosearch(){
	console.log("gosearch执行")
	/*一行开头是括号或者方括号的时候加上分号就可以了，其他时候全部不需要。其实即使是这两种情况，在实际代码中也颇为少见。*/
	var keyword=$('#search-input').val()
	console.log(keyword)
	if (keyword != "") {
		$.ajax({ 
		url: 'http://127.0.0.1:8000/index/keyword',
		//dataType: 'json',
		type: 'POST',
		async: false,
		//data:JSON.stringify(obj),
		data:{"keyword":keyword},
		success: function(data) {
			//alert("传递数据成功！");
			console.log(data)
			window.location.href='http://127.0.0.1:8000/search/';
			window.event.returnValue=false
			//alert("是否跳转")
			//alert(data)
		},
		error: function () {
			console.log("error");
			alert("传递数据失败！");
		}
	});
	}
	else {
		alert("Enter a keyword into the search box");
		console.log("do something");
	}
}