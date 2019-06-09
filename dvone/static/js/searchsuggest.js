window.onload =
  function () {
    loadlist();
 }

function
loadlist(){
	$.ajax({
    url: 'http://127.0.0.1:8000/searchsuggest/',
    type: 'POST',
    async: true,
    success: function (result) {
      console.log(result);//.data
      postTemplate(result);//.data
    },
    error: function (xhr) {
      console.log("没有数据！");
    }
  })
}

/*<li class="list-item">
    <div class="list-content" id="1851857" onclick="dvinterface(this)">
      <h2>蝙蝠侠：黑暗骑士</h2>
      <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p462657443.jpg" alt="" />
      <p>The Dark Knight-2008</p>
      <a href="https://movie.douban.com/subject/1851857/?suggest=%E9%BB%91%E6%9A%97%E9%AA%91%E5%A3%AB">豆瓣界面</a>
    </div>
  </li>*/
  /*{
    "episode": "",
    "img": "https://img3.doubanio.com/view/photo/s_ratio_poster/public/p462657443.jpg",
    "title": "蝙蝠侠：黑暗骑士",
    "url": "https://movie.douban.com/subject/1851857/?suggest=%E9%BB%91%E6%9A%97%E9%AA%91%E5%A3%AB",
    "type": "movie",
    "year": "2008",
    "sub_title": "The Dark Knight",
    "id": "1851857"
  },*/
function postTemplate(data) {
  //var resultlist = JSON.parse(data);
  resultlist=data
  console.log(resultlist)
  $('#searchsuggest-list').html('');
  $.each(resultlist, function (index, item) {
    $('#searchsuggest-list').append($('<li>')
    	.attr('class','list-item')
      .append($('<div>')
      .attr('class','list-content')
      .attr('id',item.id)
      .attr('onclick','dvinterface('+JSON.stringify(item)+')')
      .append($('<h2>').append(item.title))
      .append($('<img>').attr('src',item.img).attr('alt','""'))
      .append($('<p>').append(item.sub_title+"-"+item.year))
      .append($('<a>').attr('href',item.url).append("豆瓣界面")))
      )
  })
}

function 
dvinterface(item){
  $.ajax({
    url: 'http://127.0.0.1:8000/dv/chosedid',
    type: 'POST',
    async: true,
    data:{"id":item.id},
    success: function (result) {
      console.log(result);//.data
      console.log("传递id成功！");
      window.location.href='http://127.0.0.1:8000/dvresult/';
    },
    error: function (xhr) {
      console.log("传递id失败！");
    }
  })
}