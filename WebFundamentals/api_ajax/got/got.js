$(document).ready (function() {
  $(document).on("click","img", function(){
    var imgid = $(this).attr("id");
    $.get("http://www.anapioficeandfire.com/api/houses/"+imgid, function(res) {
      var html_str = "<h3>House Details</h3>";
      html_str += "<p>Name:"+ res.name +"</p>";
      html_str += "<p>Words:"+ res.words +"</p>";
      html_str += "<p>Titles:" + res.titles +"</p>"      
      $("#stats").html(html_str);
    }, "json");
  });
});






// http://anapioficeandfire.com/api/