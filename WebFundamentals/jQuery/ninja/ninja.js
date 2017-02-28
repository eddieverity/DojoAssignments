$(document).ready (function() {
  $(".ninja").click(function() {
    $(this).css("visibility","hidden");
    });
  $("button").click(function() {
    $(".ninja").css("visibility","visible");
  })
});