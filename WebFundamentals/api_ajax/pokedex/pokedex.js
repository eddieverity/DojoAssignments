$(document).ready (function() {
  function getPoke_index() {
    for (i=1;i<152;i++) {
      var format = "<img src='http://pokeapi.co/media/img/"+i+".png' class='"+i+"'>";
      
      //
      //$('#stats img:last-child').attr('desc', i); 
      //
      $("#container").append(format);
      
    };
  };
  getPoke_index();

  $(document).on("click","img", function(){
    var imgclass = $(this).attr("class");
    $.get("http://pokeapi.co/api/v1/pokemon/" + imgclass + "/", function(res) {
      var html_str = "";
      console.log(res)
      html_str += "<h4>"+ res.name  +"</h4>";
      html_str += "<img src='http://pokeapi.co/media/img/" + imgclass + ".png'>";
      html_str += "<h5>Types</h5>"; 
      for(var i = 0; i < res.types.length; i++) {
          html_str += "<li>" + res.types[i].name + "</li>";
      }
      html_str += "</ul>";
      html_str += "<h5>Height</h5>";
      html_str += "<p>"+ res.weight +"</p>";
      html_str += "<h5>Weight</h5>"
      html_str += "<p>" + res.height +"</p>"
      
      $("#stats").html(html_str);
  }, "json");



  }); 


});