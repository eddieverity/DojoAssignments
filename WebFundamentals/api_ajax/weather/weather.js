$(document).ready (function() {
  $(document).on("click","#search", function(){
    var city = $(".city").val();
    
    $.get("http://api.openweathermap.org/data/2.5/weather?q="+city+"&&appid=d1ba00c893684d9bb514682c859ca405", function(res) {
    
    console.log(res);

// http://api.openweathermap.org/data/2.5/weather?q=chicago&&appid=d1ba00c893684d9bb514682c859ca405

}, "json");



  $("form").submit(function(){
    return false;
  });















});
});