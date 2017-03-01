


$(document).ready (function() {
  $("#submit").click(function(){
    var first_name = $(".first_name").val();
    var last_name = $(".last_name").val();
    var email = $(".email").val();
    var phone_number = $(".phone_number").val();
    var format = "<tr><td>" + first_name + "</td><td>" + last_name + "</td><td>" + email + "</td><td>" + phone_number  + "</td></tr>";
    $("table").append(format);
    console.log(format)
  });  
  $("form").submit(function(){
    return false;


  });
});

// is it making two rows because i have a ".click" set to a form element of a submit? (where submit might already has some built-in functionality).

//tried pasting line6-11 into the .submit function on line 14, broke functionality (tried before & after the 'return false' on line 15)

//console.log of format variable only lists elements once