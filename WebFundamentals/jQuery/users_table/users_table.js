


$(document).ready (function() {
  $("#submit").click(function(){
    var first_name = $(".first_name").val();
    var last_name = $(".last_name").val();
    var email = $(".email").val();
    var phone_number = $(".phone_number").val();
    var format = "<tr><td>" + first_name + "</td><td>" + last_name + "</td><td>" + email + "</td><td>" + phone_number  + "</td></tr>";
    $("table tbody").append(format);
    console.log(format)
  });  
  $("form").submit(function(){
    return false;
  });
});

// is it making two rows because i have a ".click" set to a form element of submit? (where submit might already has some built-in functionality).

//tried pasting line6-11 into the .submit function on line 14, still twice

//console.log of format variable only lists elements once