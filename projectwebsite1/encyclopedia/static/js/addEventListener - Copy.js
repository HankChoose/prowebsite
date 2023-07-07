
$(document).ready(function() {
  var searchInput = document.getElementById('search-input');
  //print("ttt");
  console.log('Hello, world!');
  //window.print("ttt2")
  searchInput.addEventListener('input', function() {
    const inputValue = searchInput.value;
    console.log('inputValue:'+inputValue);
    // 发送Ajax请求到后端
    fetch('/search', {
      method: 'POST',
      body: JSON.stringify({ query: inputValue }),
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': '{{ csrf_token }}',  // 添加 CSRF Token（如果需要）
      }
    })
    .then(response => response.json())
    .then(data => {
      // 处理后端返回的数据
      console.log(data);
    })
    .catch(error => {
      console.error(error);
    });
  });
  
});
