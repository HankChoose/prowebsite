$(document).ready(function() {

  var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
  console.log("AddEvent-test1");
	$('#search-input').on('input', function() {
    //window.location.href = "http://localhost:8000/";
		var query = $(this).val();
    console.log("query="+query);
    var listContainer = $('#list-container');
		$.ajax({
			url: '/search',
      type:"post",
			data: {
				'query': query,
				'csrfmiddlewaretoken': csrfToken  // 将CSRF令牌添加到请求数据中
			},
			dataType: 'JSON',
      //dataType: 'text',
			success: function(data) {
				console.log("data0="+data);
        //var listData = response.list_data;
        
        // 清空列表容器
        listContainer.empty();

        // 将列表数据添加到容器中
        
        $.each(data, function(index, item) {
          var item_url="wiki/"+item
          var link = $('<a>').attr('href', item_url).text(item);
          var li = $('<li>').append(link);
          listContainer.append(li);

        });
        
			},
      //success: function(response) {
				//console.log("OK");
			//},
      error: function(xhr, status, error) {
        // Handle errors
        console.error(error);
      }
		});
	});
});