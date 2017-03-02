$(document).ready (function() {
  function getPoke_index() {
    for (i=1;i<152;i++) {
      var format = "<img src='http://pokeapi.co/media/img/" + i + ".png'>";
      $("#container").append(format);
    };
  };
  getPoke_index();
});