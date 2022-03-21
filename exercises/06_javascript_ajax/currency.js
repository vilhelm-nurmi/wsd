function getData(){
  var date = document.querySelector("#date").value;
  $("#currencies tr").remove();
  $.ajax(
  {
  type: "GET",
  dataType: "jsonp",
  url: "http://acos.cs.hut.fi/wsd-currency/" + date,
  contentType: "application/json",
  success: function(data){
    $.each(data, function(key,value){
       $("#currencies").append("<tr><td>" + key + "</td>" + "<td>" + value + "</td>" + "</tr>");
    });
  }
  });
}