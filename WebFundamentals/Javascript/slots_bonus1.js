function slots(tries,threshold) {
  for (var i = tries;i>0;i--) {
    var one_to_onehundred = ((Math.floor(Math.random()*100+1)));
    if (one_to_onehundred === 100) {
      var winnings = ((Math.floor(Math.random()*50+51)));
      var i = i+winnings;
      if (i>=threshold) {
        console.log("You win " + winnings + " quarters, this brings your total to " + i + " which is hits your threshold!");
        break;
      }
      else {
      console.log("You win " + winnings + " quarters, this brings your total to " + i);
      } 
    }
  }
console.log("GAME OVER");
}
slots(100,200);