$(document).ready (function() {
  $("#submit").click(function(){
    var first_name = $(".first_name").val();
    var last_name = $(".last_name").val();
    var description = $(".description").val();
    var format = "<div class='card'><h4>" + first_name + "&nbsp &nbsp &nbsp" + last_name + "</h4><button class='card_button'>Click for description!</button>";
    $("#card_container").append(format);
    $('#card_container div:last-child').attr('desc', description);
  });
  $("form").submit(function(){
    return false;
  });
  $(document).on("click",".card_button", function(){
    $(this).parent().html($(this).parent().attr("desc"));
  }); 
});
